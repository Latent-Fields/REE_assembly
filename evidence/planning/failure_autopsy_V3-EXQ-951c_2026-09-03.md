# Failure autopsy — V3-EXQ-951c (MECH-320 v_t-floor diagnostic, SD-054)

**Generated:** 2026-09-03T20:04:14Z · **Scope:** single · **Status:** confirmed at the /failure-autopsy Step 8 interactive gate, 2026-09-03
**Claim:** MECH-320 · **`experiment_purpose: diagnostic`** · **Machine-readable:** `failure_autopsy_V3-EXQ-951c_2026-09-03.json`

---

## 1. Why this run needed an autopsy at all

It **passed**, carried no adjudication flag, and self-reported a clean answer: `vt_floor_driven_by_low_v_raw`. It is here because `experiment_purpose` is `diagnostic`, and a diagnostic's self-routed label is a hypothesis about what the run found, never a verdict. That rule earned its keep on this run.

## 2. The classification could only come out one way

`ree_core/policy/tonic_vigor.py` computes:

```
v_t = max(v_t_floor, max(0.0, v_raw) * gate_e * gate_d * gate_p)
```

In **all 9 P2 cells (27,000 ticks)**, `gate_energy`, `gate_drive` and `gate_pe` each read `mean == min == max == 1.0` — exactly, not approximately. With the gate product at 1.0, `v_t == floor` **entails** `max(0, v_raw) <= floor`, which is precisely the probe's `raw_caused` branch condition.

So `gate_caused` had **zero reachable ticks in P2, at any sample size.** The reported 0/25787 restates the measured gate state; it does not adjudicate a contest between two live causes.

**The correct characterisation is "correct but non-discriminating", not "vacuous".** The gate state is *measured*, not assumed, so the run is not empty — it establishes, correctly, that the gates never engage. What it cannot support is the framing that it determined raw-versus-gate causation, because gate-caused was never on the table.

The branch is not dead in general: in **P1 training** — instrumented but excluded from the pool — the gates did move and `gate_caused` fired on 2 of 6348 floor-hits on seed 43.

## 3. Nothing in the gate could have caught this

`criteria_non_degenerate` has exactly one key: `gate_caused_classification`, defined as `bool(sufficient_sample and gc_frac is not None)` — sample size and a non-null denominator only. Nothing tests outcome reachability. The PASS verdict reduces to *"there were at least 30 floor-hit ticks."*

A smoke test could not have caught it either: the post-fix `--dry-run` produced the **identical** label, because the emitted label is reachable and only the alternative is not.

`ANCHOR_REACHABILITY_EXEMPT` is defined at driver lines 193–202 but never referenced and never emitted; its text argues reachability of the two *preconditions*, not of the two classification *outcomes* — a reachability guard aimed at the wrong object. The driver also carries no `=== HYPOTHESES UNDER TEST ===` / `=== INTERPRETATION GRID ===` block, unlike ten other drivers in the corpus.

## 4. What the run does establish, non-degenerately

1. **`v_raw` is negative on every tick for two of three seeds.** On seeds 42 and 45, `v_raw` max is **exactly 0.0** in all six cells (means −14.26 and −22.97). So `max(0, v_raw)` is 0 and `v_t` is pinned at the floor **before any gate is consulted**.
2. **`action_density` reads 1.0 in all 9 cells** — a vigor bias has no headroom to raise action rate.
3. **The gates are pinned open on the uncalmed bed too.** An earlier draft of this autopsy attributed the pinning to this run's bed calming (`num_hazards` 4→0, `proximity_harm_scale` 0.1→0.0, `hfa_guard` 0.3→0.0). That is **refuted** by the predecessor's own manifest: V3-EXQ-951, on the *uncalmed* bed, shows `gate_product_mean` = 1.0 in all 18 occurrences. The gate thresholds (`drive > 0.7`, `energy < 0.2`, `pe > 1.0`) are simply never met by this substrate's dynamics on either bed. The corrected finding is **stronger** than the bed story it replaces.

## 5. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | untested | classification correct but non-discriminating |
| Biological reference | clear | Niv 2007 / Beierholm 2013 average-reward-rate vigor; not the failure locus |
| Prerequisites | present | both preconditions met with wide margins |
| Implementation | complete but pinned | `v_t` pinned at floor by negative `v_raw` |
| Environment | wrong pressures — but **not** from this run's bed change | gates pinned on both beds |
| Measurement | misleading | the sole non-degeneracy key tests sample size, not reachability |
| Integration | isolated | |
| Scale | adequate | 25,787 pooled ticks — a large sample of an unreachable contrast |

**Failure location (GOV-FAILLOC-1): MIXED (MEASURES + ENVIRONMENT)** — not chargeable to REE. The mechanism was never placed in a condition where it could act.

## 6. Routing — the brake fires

**MECH-320 carries five prior non-contributory ceiling readings**, and the vigor scalar has never once moved E3 selection in any of them. V3-EXQ-951c is the second consecutive re-pose that did not deliver a DV that can move. MECH-320's own stated re-check condition — *"a re-posed successor with a DV that can move"* — is **not met**: `action_density` is still 1.0 in all nine cells.

**A sixth same-claim behavioural re-test is REFUSED.** Routing is `/implement-substrate`. A redesign testing a *different* mechanism under a new EXQ number remains permitted.

**Substrate — `amend` the MECH-320 entry.** Its sole existing failure_record item already records the same gap from V3-EXQ-571 ("bias channel present in substrate but not propagating to E3 selection"); this run supplies the mechanism for *why*. Governance should also **set `severity: corrupting` and `substrate_paths: ree_core/policy/tonic_vigor.py`**, neither of which the entry currently carries — the defect makes every MECH-320 behavioural measurement a measurement of a pinned scalar that looks valid, which is the `corrupting` definition. (User confirmed at the Step 8 gate.)

`recommended_diagnostic_evidence_adjudicated: true` — so the zero is recorded as adjudicated-and-expected rather than as an evidence gap.

## 7. Process note for governance (not an autopsy verdict)

V3-EXQ-951's third precondition, `baseline_no_op_opportunity`, is the check that made 951 a FAIL. It is **absent from 951c**, whose driver declassifies it as "not this script's DV" — while `action_density` remains 1.0 in all nine of 951c's own cells, i.e. the condition it detected persists unchanged.

Whether a successor scoped to a different DV may drop a predecessor's blocking precondition while that condition persists is a governance question. It is stated here neutrally: an earlier draft called this "evading rather than clearing", which is stronger than the evidence supports for a diagnostic on a different DV.

## 8. Learning extracted

1. A non-degeneracy flag can certify a diagnostic while being blind to the diagnostic's actual limitation — `gate_caused_classification` tests sample size and a non-null denominator, never outcome reachability.
2. A smoke test cannot catch this class: the emitted label is reachable and only the alternative is not.
3. Calming a bed to isolate one cause *looks* like the culprit and was not here — always check the predecessor's own cells before attributing a pinning to a configuration change.
4. A reachability guard must be aimed at the *outcomes*, not the preconditions.

## 9. Red-team pass

Cross-model adversarial review (Fable). Verdict: **CONTESTED on characterisation only** — the arithmetic verified fully (9/9 cells at exactly 1.0; `v_raw` max 0.0 on all six seed-42/45 cells; the entailment airtight to `FLOOR_EPS` = 1e-9), but "VACUOUS" overstated it and the calmed-bed causal story was contradicted by 951's own manifest. Both corrections are applied above. **Routing, the brake firing, and the MECH-320 amend all survive unchanged.**
