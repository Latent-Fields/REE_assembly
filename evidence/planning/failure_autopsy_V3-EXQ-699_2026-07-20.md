# Failure autopsy — V3-EXQ-699 (re-adjudication)

**Generated** 2026-07-20T05:14:51Z · **Session** `interesting-leakey-683b5d` · **Status** confirmed
**Target** `v3_exq_699_pcomp_demotion_x_gonogo_composition_20260623T053755Z_v3` (PASS, `levers_compound`)
**Claims** MECH-448, MECH-449 · **Machine** ree-cloud-1 · **Purpose** diagnostic
**Precedent** [`failure_autopsy_V3-EXQ-708_2026-07-19.json`](failure_autopsy_V3-EXQ-708_2026-07-19.json) (REE_assembly `e0ebcbcecc`)

> **Verdict in one line.** The **PASS stands**; the **`levers_compound` finding is withdrawn**.
> This is a withdrawal, not a reversal — the corrected sign is unknown.

---

## 1. Why this is not a copy of the 708 autopsy

The commissioning brief assumed 699 was the same defect as 708. It is the same *class* and a
different *mechanism*, and the difference changes the adjudication at both ends.

| | V3-EXQ-708 | V3-EXQ-699 |
|---|---|---|
| Diagnostics latch | genuinely never refreshed | **reassigned every `select()`** (`e3_selector.py:2452`, demotion key pre-seeded `False` at `:2511`) |
| Read cadence | once per env step | once per env step (**same**) |
| Nature of defect | staleness **+** replication | **replication only** |
| `active_frac == 1.0` means | vacuous (latched) | **gate fired on every E3 tick** (informative) |
| Load-bearing gate | the contaminated DV itself | readiness only — the DV is the *finding*, not a criterion |
| Margin to flip | 0.26–0.37 nats — unreachable | **0.11–0.13 nats against 0.18–0.19 of headroom — reachable** |
| Claim exposure | `epistemic_category` had to be cleared | **none** — claims rest on 689d/689g |

`_go_nogo_eligibility_gate` (`:1145`) is invoked at `:2878`, i.e. *after* the reassignment, so its
keys are absent (→`False`) on any E3 tick where the gate does not fire. Diagnostic **values are
fresh**. What is replicated is the *reading*, once per env step, of a per-selection quantity.

---

## 2. Facts

Primary DV `committed_class_entropy_nats` is accumulated at driver
[`:882`/`:899`](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_699_pcomp_demotion_x_gonogo_composition.py#L882)
from `int(action[0].argmax())` on the action **returned** by `agent.select_action`. On a non-E3
tick [`agent.py:5430`](https://github.com/Latent-Fields/ree-v3/blob/main/ree_core/agent.py#L5430) returns the **held** action before
`e3.select()` is reached. Cadence defaults to 10 steps (`config.py:2017`) and varies 5–20 under
MECH-093 arousal modulation (`clock.py:52-70`).

**Three exposures, only one of which the lint sees:**

| Site | Quantity | Flagged by `validate_experiments`? |
|---|---|---|
| `:882` | `committed_class` — **the primary DV** | **no** |
| `:913` | `_last_selected_trajectory` → `selected_class`, within-class-rep control | **no** |
| `:929` | `last_score_diagnostics` | yes — the only one |
| `:856` | `pre_e3_classes` (candidates are also `e3_tick`-gated, `agent.py:4812`) | no |

**Empirical confirmation.** `selected_class_entropy_nats == committed_class_entropy_nats` **to 6dp
on all 12 arm-seeds**. Two nominally independent readouts are the same number — the design's
internal cross-check is vacuous.

---

## 3. What survives: C1, and therefore the PASS

The single load-bearing criterion is `C_READY_levers_engaged_and_substrate_exercisable`
(`interpretation.criteria` — one entry, `load_bearing: true`). It survives on **threshold
invariance**, not on the falsified "means are invariant under uniform replication" argument:

- **`excluded_count_floor = 0.0` and `nogo_suppressed_floor = 0.0`.** A strictly-`> 0` test is
  invariant in both directions — duplication cannot manufacture a positive from an all-zero record,
  nor collapse a genuine positive to exact zero. This is 708's own argument. Measured **14.81** and
  **0.69** against `0.0`.
- **`active_frac` and `frac_pre_ge2` read exactly `1.0`.** Given the per-`select()` reassignment,
  exactly 1.0 *requires* firing on every E3 tick. Saturated ⇒ invariant.

Both levers demonstrably did real work. **C1 holds; the PASS is untouched.**

---

## 4. What does not survive: `levers_compound`

### 4a. Construct mismatch

The driver's own framing (lines 88–97) is *"the levers move **which class is committed**"* — a
per-**commitment** construct — and MECH-448/449 both act at **selection**. Reading the class once
per env step weights each commitment by its **hold duration**, so the DV becomes selection
diversity convolved with perseveration duration. Neither lever claims to act on hold duration.

The occupancy entropy is a *genuine* measurement of one thing and an *invalid* measurement of the
thing the claims are about.

### 4b. The bias is aligned with the hypothesis — no sign-check is available

ARM_OFF is the reference for **every** delta. If the unarmed agent perseverates more — the expected
consequence of removing two selection-perturbing levers, via the same MECH-093 coupling 708 invokes
— its holds are longer, its occupancy entropy is systematically **depressed**, and every `d_*` is
**inflated**, `d_both` included.

708 was condemned by a mechanistically-*backwards* sign, which is a detector. Here the bias points
the **same way as the effect under test**, so the finding cannot be rescued as "imprecise but
directionally right".

*Consistent with, but not proof of, the mechanism:* OFF carries the lowest entropy in 2 of 3 seeds
and the fewest unique classes in seed 43 (2, vs 4 on ARM_BOTH) — equally consistent with the levers
genuinely working. **That is the confound, stated precisely.**

### 4c. Margin arithmetic — and it runs the opposite way to 708

COMPOUND requires `d_both ≥ max(d_dem,d_gng)+0.05` **and** `d_both ≥ 0.05`, on ≥2 of 3 seeds.

| seed | d_dem | d_gng | d_both | verdict | max-rule slack | lift-floor slack |
|---|---|---|---|---|---|---|
| 42 | 0.0180 | 0.1415 | 0.0868 | neutral | −0.1047 | 0.0368 |
| 43 | −0.3057 | −0.5112 | 0.1843 | compound | 0.4400 | **0.1343** |
| 44 | 0.0065 | −0.2839 | 0.1647 | compound | 0.1082 | **0.1147** |

Seed 42 is already neutral, so **killing either remaining seed → NEUTRAL** (`n_compound` 1 < 2).

**Which rule binds.** A common shift in `e_off` moves `d_both`, `d_dem` and `d_gng` *equally*, so
the max-rule slack is **invariant** to it. The binding constraint under the §4b correction is
therefore the absolute floor `d_both ≥ 0.05`:

| seed | correction needed | headroom available |
|---|---|---|
| 44 | `e_off` under-estimated by **0.1147** | `0.9097 → ln3 = 1.0986` ⇒ **0.1889** |
| 43 | `e_off` under-estimated by **0.1343** | `0.5112 → ln2 = 0.6931` ⇒ **0.1820** |

Both requirements sit **inside** the headroom. And `e_both(43) = 0.6955` is already at its effective
two-class ceiling (5821/5365 + two singletons), so under de-weighting it can only **fall** — pushing
the same direction. Contrast 708, whose seeds were 0.26 and 0.37 nats short, *"which no
de-duplication correction can supply."*

### 4d. Why the "<1%, sign-varying" 663 measurement does NOT cover this run

Session `mech-279-evidence-confirm-8f3087` (2026-07-20T06:25Z, ree-v3 `5433e3ab1c`) **measured** this
defect's cost on the `v3_exq_663_modulatory_channel_routing` driver by matched replay: **+0.01% /
+0.64% / −0.87%** on `route_range_mean` — sub-1% and sign-varying, so 662/663's point estimates and
PASS **stand**. That is a real, welcome result. It must not be generalised to 699:

1. **Different statistic class.** 663's DV is a continuous *magnitude* (`route_range`) read at the
   selection site. Replicating a value leaves a mean of that value essentially unchanged. 699's DV is
   an **entropy over a class histogram** — replication reweights the *distribution itself*, which is
   exactly the operation entropy is sensitive to.
2. **Different arm symmetry.** 663's replication is near-uniform across its arms, so it cancels in
   the contrast. 699's arms differ in **hold duration** — the very quantity doing the weighting
   (§4b) — so it does not cancel and is aligned with the effect.
3. **Different magnitude relative to the margin.** 663's artifact is 1–2 orders of magnitude *below*
   the +12–25% cross-class gaps under test. 699's flip requires only 0.115–0.134 nats against
   entropies of 0.51–1.10 nats — **roughly 12–26%**, i.e. 1–2 orders of magnitude *above* the 663
   artifact scale.

663 measured the artifact **where it cancels**; 699 sits where it does not. The 663 replay is
nonetheless the right instrument — requirement 3 in §9 asks 699b to run the same matched-denominator
comparison, which would settle this by measurement rather than argument.

### 4e. What cannot be established

The **replication factor is not observable from the manifest.** `n_p2_ticks` (seed 44:
525/1737/461/707, a 3.8× span) counts **env steps** and is driven by episode termination, not
directly by E3 cadence. The chip cited that span as arm-dependent exposure; it is a real step-count
fact but **does not by itself demonstrate an arm-dependent replication factor**. The honest
statement is that the weighting is unobservable and the contamination unbounded — not that a
specific distortion was measured.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact, untouched | both claims rest on 689d/689g; this run promotes nothing |
| Biological reference | clear | BG direct/indirect opponency; not load-bearing — failure is at measurement |
| Prerequisites | present | all 7 preconditions pass, C1e/C1f on invariant grounds |
| Implementation | complete | levers fired and did real work (14.81 excluded; 0.69–12.41 suppressed) |
| Environment | adequate | not implicated |
| **Measurement** | **misleading — DOMINANT** | hold-weighted occupancy standing in for per-commitment selection |
| Integration | isolated | not implicated |
| Scale | unknown | unassessable through a contaminated DV |

**Recommended `epistemic_category`:** `measurement_test_design_defect`.
**`evidence_direction`:** `non_contributory` — **unchanged** (it was already that on both claims).

---

## 6. Claim layer — nothing is cleared

The sharpest contrast with 708. MECH-440 carried `epistemic_category: substrate_ceiling` whose
*sole* basis was 708's withdrawn DV, so it had to be cleared. Here **neither claim's
`evidence_quality_note` cites V3-EXQ-699 at all** — MECH-448 rests on V3-EXQ-689d, MECH-449 on
V3-EXQ-689g, both `status: provisional`, `epistemic_category: standard`.

**Action: append the note to both claims. Change nothing else. No confidence moves.**

### Illusory-conflict check (mandatory pairing)

Withdrawing this removes the only V3 evidence that the two levers are **safe to co-arm**. Each
solo validation survives, so neither claim narrows — but any downstream plan that co-arms both on
the strength of 699 is now **unsupported**. Note the question is open *in both directions*: the
design's own CANCEL branch (the destructive Factor-A × Factor-B 689a signature) was **also** never
ruled out by an uncontaminated measurement. Do not restate "the levers compound" or "safe to
co-arm" pending 699b.

---

## 7. Recoverability — no

No `custom_information`, no per-tick sink, `metrics.json` = **53 chars**, ran on **ree-cloud-1**
(Phase 3 transports `manifest_bytes` only — now **thrice-confirmed** with 785 and 708). The
replication factor cannot even be *estimated*. A corrected re-run is required.

---

## 8. Gates

- **Re-derive brake: NOT FIRED.** MECH-448 and MECH-449 each have **0** prior
  `substrate_ceiling`/`non_contributory` autopsy targets. Recommended category is
  `measurement_test_design_defect`, so even counting this document the rule is not met.
- **Granularity-debt trigger: NOT FIRED.** No prior autopsy targets 699 / MECH-448 / MECH-449.
- **Step 9b (frozen ledger): skipped cleanly.** No `fanout_recommendation` (single unambiguous
  instrument repair, not a discrimination), and no registry question or leg references 699 /
  MECH-448 / MECH-449 — nothing to pre-register, nothing to resolve, no denominator to move.

---

## 9. Routing → `/queue-experiment` as **V3-EXQ-699b**

**Naming dissent, recorded.** The commissioning chip instructs a *new EXQ number*. This autopsy
recommends an **alphabetic suffix**. CLAUDE.md is explicit that *"bug fix = the scientific question
is unchanged but the implementation was wrong (broken instrumentation…)"* takes a letter, and
*"when in doubt: new letter"*; the 708 precedent used `708a` for this same class of repair. The
chip's "changes the statistics" reasoning was authored to justify keeping the **699a re-run
faithful**, not to govern the naming of a corrected successor.

Requirements (full list in the JSON):

1. **Clear before select.** `last_score_diagnostics = None` **and** `_last_selected_trajectory =
   None` immediately before every `select_action(...)`; record only on repopulation. Pattern:
   `v3_exq_785a_...py:525-543`.
2. **Emit `n_fresh_select` / `n_latched` / `fresh_select_yield`** — the single field whose absence
   made 699 unrecoverable.
3. **Emit BOTH readouts, kept distinct:** per-commitment class entropy (the verdict DV) *and*
   hold-weighted occupancy entropy (what 699 measured). This makes the size and direction of this
   defect measurable across the corpus for the first time.
4. **Record per-arm-seed hold-duration distribution** — directly tests the §4b alignment argument.
5. **Drop `selected_class_entropy_nats`** — identical to the primary DV on every cell.
6. **Keep the C1 battery unchanged** — it is sound and worth reproducing exactly.
7. `supersedes: V3-EXQ-699` (and 699a if it completes first); `stamp_recording_core(...)`.

---

## 10. In-flight: V3-EXQ-699a — **not touched**

`status: claimed` by **ree-cloud-3** at 2026-07-19T21:05:38Z, ~600 est. minutes, priority 5, running
the **unchanged** driver.

**This session took no action on it.** Releasing or dequeuing a claimed item goes through the
coordinator and requires the user's explicit go-ahead, which was not obtained.

**Assessment.** 699a will reproduce every defect above — it is the same driver. Its purpose
(repairing the precondition-*declaration* bug, ree-v3 `0bfbb42`) is real, but note what it buys: it
cleanly re-emits the **C1 readiness gates, which this document finds already survive**, while
re-emitting a **primary DV that does not**. The repair is to the reporting of the part that was
never in danger.

**Recommendation — DEQUEUE** and replace with 699b, which inherits the `0bfbb42` fix automatically
(it is prospective and already on `main`). Saves ~600 min and avoids landing a second manifest
carrying a withdrawn finding.

> **If instead it is allowed to finish, its manifest MUST carry this document's
> `evidence_quality_note` verbatim.** Otherwise a cleanly-adjudicable `levers_compound` lands on the
> record and reads as *confirmation* of the very finding withdrawn here — the worst available
> outcome.

**Queue-note correction.** The 699a entry's KNOWN CAVEAT asserts the readiness gates are *"RATIOS
and MEANS … invariant under uniform replication, so the PASS is not threatened."* The premise is
**falsified** (708 established replication is arm-dependent); the conclusion happens to hold for the
different reasons in §3. That paragraph must not be cited as authority in any successor entry.

---

## 11. Learning extracted

1. **The 708 defect class has a second form the lint cannot see.** The lint keys on
   `last_score_diagnostics`; 699's load-bearing exposure is the **committed action itself**. Any
   driver accumulating a per-step statistic from the **return value** of `select_action` inherits
   hold-duration weighting without touching a diagnostics latch. **The affected-corpus sweep should
   be re-run against this signature.**
2. **Freshness and replication are independent defects**, and conflating them mis-adjudicates in
   both directions — 699's `1.0` is informative precisely *because* its diagnostics are fresh, where
   708's identical `1.0` would be vacuous.
3. **Construct mismatch, not staleness, is the general hazard.** Ask what the *mechanism* acts on
   and require the readout's sampling unit to match it.
4. **Contamination aligned with the hypothesis is categorically worse than contamination that is
   merely large** — it removes the sign-check that condemned 708, and forces withdrawal rather than
   correction.
5. **An arm-dependent step count is not proof of an arm-dependent replication factor.** The chip
   over-claimed; record the factor instead of arguing it.
6. **Two readouts agreeing to the last decimal on every cell is a defect signature, not a
   validation.**
7. **A defective instrument can leave the PASS correct while destroying the FINDING** — adjudicate
   them separately or lose one to the other.
8. **Threshold-invariance is the reusable test**, and a floor of literally `0.0` is its strongest
   form. Gates stated as "> 0", or that saturate, are safe; continuous margins against a non-trivial
   floor are not.
