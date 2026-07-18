# Failure Autopsy — MECH-457 GOV-FANOUT-1 discrimination portfolio + shared instrumentation probe

**Scope:** CLUSTER (3 targets) · **Status:** confirmed · **Generated:** 2026-07-18T18:01:44Z
**Targets:** V3-EXQ-782 (MECH-459, probe R) · V3-EXQ-781 (MECH-457, H-approach-primitive) · V3-EXQ-780 (MECH-457, H-bc-prior)
**All three are DIAGNOSTIC. This autopsy promotes and demotes nothing.**

---

## Headline

**The portfolio eliminates one leg, not two — and the leg it does not eliminate is the more important result.**

- **V3-EXQ-781 → H-approach-primitive ELIMINATED.** Clean: manipulation effective, null readable, bar met.
- **V3-EXQ-780 → H-bc-prior STAYS ALIVE.** Its self-route `bc_prior_not_the_axis` is rejected on autopsy: the run's pre-registered null required "treat still forages ~0 both reps", and raw_view returned **11.667** at eval and **20.933** post-BC. The null's antecedent is falsified, so its consequent must not be applied.
- **V3-EXQ-782 → MECH-459 weak form WEAKENED**, and — contrary to the concern that motivated adjudicating it first — it **clears** the elimination bar for 781 rather than blocking it.

The cluster's structural finding: **the campaign has been asking a discovery question of a substrate whose deficit is retention.**

---

## 1. V3-EXQ-782 — the shared control arm (adjudicated first)

Probe R instruments the reference composed-bootstrap **CTRL** path — the shared control arm of both 780 and 781 — with no manipulation and no treatment arm, sanctioned by `decision_MECH-459_registry_and_brake_2026-07-18.md` Decision 2b. Only the **weak** form of MECH-459 is under test; the strong form was refuted by that decision's Finding V2 and is not restated.

### R-(a), load-bearing: `forage_mass_already_concentrated`

| rep | C_pre | C_post | delta | threshold |
|---|---|---|---|---|
| z_world | **1.918** | 1.575 | −0.343 | "tiny" = < 0.5 |
| raw_view | **1.203** | 1.062 | −0.141 | "tiny" = < 0.5 |

Both C_pre values are **above** the 0.5 tiny threshold, so the weak form's **premise fails**: forage-contact steps already carry disproportionate |adv| mass *before* the standardiser. There is no tiny forage signal for novelty noise to swamp. The standardiser slightly *reduces* concentration rather than amplifying noise over it.

All four readiness preconditions met (local_view_greedy 48.05, greedy_oracle 57.2, 273 forage steps vs a 30 floor, demonstrator return std 0.3027 vs a 0.25 floor); `non_degenerate: true`.

Per the probe's **own pre-declared conditional**, an already-concentrated reading routes MECH-459 to `weakened`, queues **no probe K**, and makes **no registry write** (counts stay 7/12). Honoured.

### The conditioning payoff — Finding V3 resolved favourably

The decision doc flagged that 781's approach drive enters `shaped` **inside** the normaliser, so a 781 null would have been confounded **if the weak form held**. It does not hold. Therefore:

- **781's null is readable at face value.**
- **780 was never confounded** — its BC auxiliary is a loss-side CE term outside the normaliser.

So 782 **clears** the bar for the portfolio. This is the outcome the pre-registered conditional was written to detect.

### R-(b), declared non-load-bearing: `critic_flat_uninformed`

| metric | z_world | threshold |
|---|---|---|
| std(V) / std(G) | **0.041** | collapse if < 0.25 |
| pre-reward vs far separation ratio | **0.016** | floor 0.25 |
| value-return correlation | 0.434 | — |

The critic is **flat and uninformed** (signal-absence), *not* collapsed-to-the-bimodal-mean. Note the dissociation: R-(a) **exonerates** the normaliser half of MECH-459's DreamerV3 import while R-(b) **corroborates** the distributional-critic half of that same import's prescribed corrective. A composite algorithmic-import claim must be adjudicated half by half.

This becomes the leading mechanism candidate for 780's erosion. It licenses **no build** — not the twohot critic, not the percentile normaliser.

### Substrate equivalence caveat (checked, not waved through)

782's `substrate_hash` (`098473b9…`) **differs** from 780/781's (`39b488c1…`). The manifest explains this by construction (instrumentation is a separate mirror module; the live scripts are byte-unchanged). Since a differing hash would otherwise make the conditioning read unfalsifiable, it was verified **behaviourally**:

| run | CTRL z_world | CTRL raw_view |
|---|---|---|
| V3-EXQ-780 | 0.650 | 7.217 |
| V3-EXQ-781 | 0.300 | 2.983 |
| **V3-EXQ-782** | **0.517** | **6.483** |

782's control arms sit inside the bands set by the other two, on shared anchors (local_view_greedy 48.05, greedy_oracle 57.2, random_walk 0.933). The mirror is behaviourally equivalent; the conditioning read transfers.

---

## 2. V3-EXQ-781 — H-approach-primitive: clean elimination

Manipulation: an innate, **non-extinguishing, demonstrator-free** appetitive resource-proximity drive (`approach_coef=1.0`) on the non-regressed reference build.

| rep | ctrl | treat | delta | seeds supra-target |
|---|---|---|---|---|
| z_world | 0.300 | 0.317 | +0.017 | 0/3 |
| raw_view | 2.983 | **0.200** | **−2.783** | 0/3 |

Against a 1.0 competence floor and a 13.05 lift-competence target. Declared null ("treat still forages ~0 both reps") — **antecedent satisfied**.

The elimination is trustworthy on three independent checks:

1. **Manipulation effective.** The script's own declared covariate — `mean_approach_reward_recent`, documented as "confirms the drive fired (a null with a live drive is informative, not a plumbing bug)" — reads **0.698 / 0.707** in treat vs **0.000** in both ctrl. The drive fired and was continuously earned.
2. **Null readable.** 782 R-(a) removes the weak-form confound (above).
3. **Substrate can express competence.** 780's raw_view arm reaches **20.933** on this same substrate when a competent policy is installed — so the null is not a can't-express-it artifact. **781 did not contain this positive control internally; only joint adjudication supplies it.**

### Load-bearing positive finding: approach without consummation

In raw_view the drive **suppressed** foraging — 0.200 against a 2.983 control — while approach reward was earned throughout. The effect is reliable, not seed noise: treat per-seed is tight (0.15 / 0.20 / 0.25) while the control mean rides on a single outlier (0.30 / 0.55 / **8.10**).

The agent learned to **approach and dwell rather than consume**: the appetitive drive became *terminal* instead of *instrumental*. In real foraging, appetitive approach is bound to a consummatory response. This is a discovered dependency — a consummation/commitment binding — and it converges with the standing basal-ganglia-commitment reading of the conversion ceiling rather than opening a new axis. That convergence is why no new hypothesis leg is registered for it.

---

## 3. V3-EXQ-780 — H-bc-prior: self-route REJECTED, leg stays alive

Manipulation: a competence-directed **behavioural prior** (BC warm-start + persistent imitation auxiliary, `bc_aux_coef=0.5`, demonstrator `local_view_greedy`).

The script's `load_bearing_dv` declared the covariate that decides this run: *"post_bc_foraging_competence separates 'seed never took' from 'seed erased by RL'."* **It fires unambiguously, into two branches — and neither branch is `bc_prior_not_the_axis`.**

| rep | post-BC forage | bc_seed_took | eval forage | train-recent | reading |
|---|---|---|---|---|---|
| z_world | 0.583 | **0/3** | 1.950 | 3.393 | **seed never took** — manipulation never installed |
| raw_view | **20.933** | **3/3** | 11.667 | 17.993 | **seed took above the 13.05 target, then RL eroded it** |

The pre-registered null is verbatim *"treat still forages ~0 both reps"*. raw_view forages 11.667 at unshaped D3 eval, 17.993 train-recent, **20.933** immediately post-BC. That is not ~0. **The null's antecedent is falsified, so H-bc-prior is not eliminated.**

Readiness met; `non_degenerate: true`; `criteria_non_degenerate` all true. **The defect is in the interpretation grid, not the instrumentation** — the grid enumerated only a ~0 null, so a *successful* manipulation was scored as a null. The covariate that catches it was already present and declared; the routing logic simply did not consume it.

### Why this is the campaign's most valuable result

**20.933 is the first observation in the entire `competence_floor` campaign of the agent exceeding the lift-competence target (13.05)** on this substrate — inside the 32.72 BC-expert band, against a 48.05 local-view ceiling. Then RL pulled it down to 11.667.

That inverts the biological expectation: reward-driven refinement of an imitated skill should *improve* it. Here it *degrades* it. The inversion localises to the **value-baseline / retention pathway** — and 782 R-(b) supplies the measured candidate: a flat, uninformed critic yields an unbaselined, high-variance advantage, exactly what drifts a policy off an installed prior. **Neither run alone supports this reading; the cluster does.**

**Secondary finding:** the z_world imitation pathway is an implementation gap in its own right — a detached z_world could not absorb a `local_view_greedy` demonstrator at all (0/3, post-BC 0.583), where raw_view absorbed it 3/3 at 20.933.

---

## 4. Cluster pattern — one structural property, not three results

**The campaign has been asking a DISCOVERY question ("which mechanism produces competence") of a substrate whose actual deficit is RETENTION ("why is produced competence not held").**

All ten previously-resolved legs intervened on discovery-side mechanisms, and every one was adjudicated against a treatment arm that never left the ~0–1 floor (credit sweep 0.2–0.45; archive/return, curriculum, arbitration all collapsing to the sparse-RL baseline). **The retention deficit was structurally invisible to them: a mechanism that never produces competence cannot be observed failing to retain it.**

780's raw_view arm is the first arm to clear the target — and the deficit becomes visible in the same run. 782 R-(b) independently measures a candidate mechanism without knowing it was needed.

### Joint adjudication was load-bearing — in both directions

- Alone, **781's** elimination would have rested on no demonstration that competence was reachable in this substrate at all. 780 supplies that positive control.
- Alone, **780** would have been recorded as eliminating H-bc-prior on a self-route whose declared antecedent its own covariate falsifies.

GOV-FANOUT-1's premise — that adjudicating a leg in isolation is how a confident-but-wrong elimination enters the frozen ledger — is validated concretely here.

---

## 5. Four-layer diagnosis (cluster summary)

| Layer | 782 | 781 | 780 |
|---|---|---|---|
| Claim alignment | weakened (weak form only) | intact | intact, leg untested |
| Biological reference | partial (formal import; halves dissociate) | clear (genuine dissociation) | clear (translation worked; retention did not) |
| Prerequisites | present | present (+ positive control from 780) | present; **new prerequisite surfaced: retention** |
| Implementation | complete | complete | **partial — z_world 0/3 install failure** |
| Environment | adequate | adequate | adequate |
| Measurement | adequate, decisive | adequate | adequate but **grid under-enumerated** |
| Integration | coupled | coupled but revealing | **coupled but unstable (20.9 → 11.7)** |
| Scale | adequate | adequate | adequate |

**Recording provenance:** all three manifests carry the full always-record core (`recording_schema` rec/v1, top-level `substrate_hash`, `machine`/`machine_class`, `elapsed_seconds`, `config`, explicit `seeds` [42,43,44]). **No recording gap; no recording-debt re-run is owed.** 782's decisive readouts were correctly *run* rather than reanalysed — per-step |adv| mass fractions and trained-critic V vs realized return are intermediate training quantities recorded by no manifest (GOV-REUSE-1).

---

## 6. Frozen-ledger delta (Step 9b) — `competence_floor`

| Leg | Before | After | Bar |
|---|---|---|---|
| H-approach-primitive | alive | **eliminated** | met (control_passed + non_degenerate + met_elimination_bar all true) |
| H-bc-prior | alive | **alive (unchanged)** | **not met** — run does not discriminate the leg |

**Denominator does not move: `initial_frozen_count` stays 12** (`initial_frozen_count_at_registration` 7). No hypothesis pre-registered this cycle.

### Narrowing ratio, reported both ways (GOV-FROZEN-1)

| Basis | Alive-only | Derived surviving (incl. confirmed) |
|---|---|---|
| vs **ORIGINAL** frozen count (7) | 1 / 7 = **0.143** | 2 / 7 = **0.286** |
| vs **CURRENT** count incl. fan-out (12) | 1 / 12 = **0.083** | 2 / 12 = **0.167** |

**`convergence_class`: `refining`** — four axis families closed out; the latest growth opened fresh territory. Cited per GOV-FROZEN-1, which is why both denominators are reported.

**Non-convergence caveat.** The question has accumulated two labelled fan-out growth events and this cluster opens the case for a third (deferred). A question accumulating fan-out events is one whose campaign has not converged — and the honest reading here is stronger: **the campaign was posing the wrong question shape for all ten previously-resolved legs.** The reduction ratio improving to 10/12 should not be read as approaching an answer.

### Why nothing was pre-registered this cycle

782's manifest pre-declared, *before it ran*, that an already-concentrated reading routes to "do NOT queue probe K, **no registry write** (counts stay 7/12)". Honoured. Registering a retention leg here would also enlarge the surviving numerator with an unadjudicated leg — the exact laundering the sanctioning decision flagged when it declined H-return-scale (adding it would have moved the ratio 0.167 → 0.231 purely by padding). The retention portfolio is carried as a **recommendation**; the `/queue-experiment` that *designs* it pre-registers its legs at fan-out time.

---

## 7. Routing

### V3-EXQ-782 → governance: weaken MECH-459 (weak form). No build licensed.
### V3-EXQ-781 → governance: record the H-approach-primitive elimination. MECH-457 unchanged.
### V3-EXQ-780 → `/queue-experiment`: **retention re-pose, NEW EXQ number.**

**Re-derive brake — permits, and here is why.** MECH-457 carries **6** prior `substrate_ceiling`/`non_contributory` autopsies, far past the threshold of 2. The brake nonetheless permits this re-pose, on the same grounds it permitted 780 and 781 themselves: it is not another config/env/credit/capacity letter circling the same ceiling. It is a **different question** (retention of installed competence, not discovery of it), with a different null, a different measurement (competence *trajectory* post-installation, not terminal competence), and — decisively — a **positive control no prior leg possessed** (raw_view reached 20.933). Every one of the 6 braked autopsies adjudicated a treatment arm that never left the ~0–1 floor. This one adjudicates an arm that reached 20.933 and fell.

**Granularity-debt trigger fires (9 prior autopsies on MECH-457; this is the 10th) but is NOT routed to `/claim-synthesis`** — MECH-457 already carries `granularity_debt_disposition: coherent_campaign`, human-adjudicated 2026-07-16 under GOV-GRAN-1. Stamped honestly so the standing scan sees a disposition, not a dropped handoff. The cluster's finding supports that disposition: the campaign is coherent and its legs are genuinely distinct rivals; what changed is the *question shape*, which is not granularity debt in the claim.

### Recommended fan-out portfolio (producer half, GOV-FANOUT-1 — for the designing session to pre-register)

| Hypothesis | Axis | Probe sketch | Null |
|---|---|---|---|
| H-retention-critic | algorithm | BC-install to the 20.9 point, then identical RL refinement with a distributional/twohot critic vs the current scalar critic | prior erodes identically under both → critic baseline is not the mechanism |
| H-retention-consolidation | policy | BC-install, then RL with a trust-region / KL-anchor to the installed policy vs unconstrained | anchoring does not preserve competence → not a drift-protection problem |
| H-retention-auxiliary-decay | learning-signal | BC-install, sweep `bc_aux_coef` persistence (constant / annealed / off), measure competence half-life | half-life invariant to schedule → prior is not being out-competed |
| H-consummation-binding | intrinsic-architecture | approach drive gated to **extinguish** on resource contact and hand off to a consummatory act, vs 781's non-extinguishing terminal drive | competence still flat → binding is not what 781 lacked |

**Anti-alias requirement:** H-retention-critic and H-retention-consolidation can both yield "competence preserved" — the design audit must keep them separable (critic probe changes the *value estimator*; consolidation probe changes the *update constraint*; a leg changing both aliases them).

**Every leg MUST record the post-installation competence trajectory, not just terminal competence.** Terminal-only measurement is precisely what kept this deficit invisible for ten legs.

**Axis-family caution (read before scoring this portfolio as circling).** Three of four proposed axes (`algorithm`, `policy`, `learning-signal`) map to the **`process`** family, which already holds 6 eliminated legs — a naive read scores this as **circling**. It is not the dead legs wearing new names, and the distinction is measurable rather than rhetorical: every eliminated process leg intervened on how competence is *discovered* and was adjudicated against an arm at the ~0–1 floor; these probes intervene on whether *already-installed* competence is *retained*, are adjudicated from a 20.933 starting point, and read a trajectory. The prior legs could not have detected a retention deficit because their arms never produced competence to retain. If the designing session introduces a `retention` axis label it **must** add a family row in `axis_families.map` in the same edit (an unmapped axis forces `convergence_class` to `indeterminate`) — and should state this reasoning explicitly rather than letting the family map decide the verdict silently.

---

## 8. Learning extracted

1. **H-bc-prior is not eliminated.** Applying a null's consequent when its antecedent is falsified would have written a confident-but-wrong elimination into the frozen ledger — the exact failure GOV-FANOUT-1 exists to prevent.
2. **A behavioural prior CAN reach lift-competence on this substrate** (20.933 > 13.05) — the campaign's first such observation. The bottleneck is not *producing* competence but *retaining* it.
3. **RL degrades an installed competent prior** (20.933 → 11.667), inverting the biological expectation. That inversion is the load-bearing divergence.
4. **782 R-(b) and 780 raw_view interlock into one mechanism** (flat critic → unbaselined high-variance advantage → policy drift). Neither run alone supports it.
5. **781: approach without consummation** — the appetitive half is instantiable but unbound to a consummatory act; converges with the BG-commitment thread.
6. **The two halves of MECH-459 dissociate** — R-(a) exonerates the normaliser, R-(b) corroborates the flat critic. Composite algorithmic-import claims need half-by-half adjudication.
7. **z_world cannot be taught by a local_view_greedy demonstrator** (0/3 install) where raw_view can (3/3 at 20.933) — a separate implementation gap.
8. **Process learning: an interpretation grid must enumerate a branch for "manipulation succeeded, then decayed."** This grid enumerated only a ~0 null, so a successful manipulation was scored as a null. **Diagnostic scripts should route on their declared covariates, not only on the terminal criterion** — the covariate was present, declared, and ignored by the routing logic.

---

*Adjudicated by session `mech457-gov-fanout-1-autopsy-3beae1` (worktree `wizardly-solomon-3beae1`). Inputs: the three manifests in `evidence/experiments/`; `claims.yaml` MECH-457 / MECH-459; `decision_MECH-459_registry_and_brake_2026-07-18.md`; `hypothesis_space_registry.v1.json` (`competence_floor`); `failure_autopsy_MECH-457-fanout-770-771-772_2026-07-18.json`; `.claude/skills/failure-autopsy/SKILL.md` Step 9b / GOV-FANOUT-1 / GOV-FROZEN-1. User scientific judgment confirmed all four routing decisions at the Step 8 gate.*
