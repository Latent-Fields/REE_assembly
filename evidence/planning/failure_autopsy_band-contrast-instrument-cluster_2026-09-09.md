# Failure autopsy — band-contrast instrument cluster (V3-EXQ-999a + V3-EXQ-981a)

**Generated:** 2026-09-09T09:37:25Z · **Scope:** cluster (2 targets, 2 claims)
**Status:** confirmed (user gate 2026-09-09, with red-team) · **Red-team verdict:** CONTESTED
**Targets:** V3-EXQ-999a (MECH-161) · V3-EXQ-981a (MECH-027)
**Dry-run gate:** both run_ids clean.

---

## 1. The finding

Two experiments on unrelated claims, both blocked at a pre-criterion positive control built on the
same high-versus-safe hazard-band contrast. In both, **the band-contrast statistic is the fragile
element, not the agent's capability** — and it fails for a different proximate reason in each run.

- **V3-EXQ-999a**: the agent's safe bin is starved (3 executable decision ticks against a floor of
  10) and 98.5% wall-clamped, so the contrast cannot be computed for the agent — while the *same
  run's* decision-tick readout puts the agent **above the hazard-blind null at 4 of 5 heartbeat
  levels**.
- **V3-EXQ-981a**: the contrast's **sign and verdict depend on the normalisation choice**, which
  the driver never justified.

Neither claim was tested. Neither run supports any conclusion about whether hazard avoidance
exists.

---

## 2. This artifact's first draft was wrong, and the correction is part of the finding

The first draft asserted a shared **substrate** gap: that the substrate trains hazard valuation and
no avoidance policy, so both positive controls were correctly reporting a capability that does not
exist. That reading is **withdrawn** on three independently verified grounds.

**(a) The capability is weakly present.** From V3-EXQ-999a's own metrics block:

| P (heartbeat) | 5 | 8 | 10 (train) | 15 | 20 |
|---|---|---|---|---|---|
| agent − null | **+0.1388** | **+0.1132** | **+0.0989** | **+0.1617** | −0.0095 |
| as % of oracle − null | 18.2% | 13.9% | 12.4% | 21.3% | −1.2% |

Above null at 4 of 5 levels. "Avoidance does not exist" is falsified by the manifest that was
supposed to show it.

**(b) V3-EXQ-981a's negative reading is normalisation-dependent.** Recomputed from the manifest's
own bin counts:

| normalisation | value | vs +0.05 bar |
|---|---|---|
| pooled **additive** lift (the gate as built) | −0.09575 | FAIL |
| pooled **ratio** lift | **+0.06282** | PASS |
| raw, mean of seeds | **+0.06226** | PASS |
| ratio, mean of seeds | **+0.08428** | PASS |

Response rates sit at 10–40% of availability, so the additive form is dominated by the
**availability gap** (chance_HIGH − chance_SAFE = +0.14307) rather than the behavioural difference
(rate_HIGH − rate_SAFE = +0.04732). The driver correctly justified moving *off* raw rates — that
was V3-EXQ-981's real defect — but never considered a multiplicative alternative, which is the
standard choice when rates are far from ceiling. **User-ratified disposition: the control is
undetermined. It neither passes nor fails, and the re-run must pre-register a normalisation with a
stated rationale and report all three.**

**(c) The avoidance-policy machinery already exists and is default-off.** `use_instrumental_avoidance`
(`ree_core/utils/config.py:5721`, SD-058/MECH-357, with `ree_core/pfc/infralimbic_avoidance_gate.py`)
and `use_escape_affordance_bridge` (`:5807`, SD-059/MECH-358). **Neither driver references either**
(grep count 0 in both). The substrate entry for it already sits at `implemented_pending_validation`.
The first draft proposed to *create* this capability and cited `scaffold_train_harm_pathway` as
precedent — which trains the **valuation** pathway, exactly what both drivers already do, so the
citation contradicted the very distinction it was offered to support. **No build is owed.**

---

## 3. What each run actually shows

### V3-EXQ-999a (MECH-161) — ree-cloud-2, 7h04m, 5 seeds × 5 levels

Two readiness gates red: `agent_safe_bin_executable_decision_ticks_covered` **3.0** vs a floor of
10 (seed23/P20), and `baseline_avoidance_clears_derived_bar` **−0.1013**. The latter is
underpowered — SD 0.3139, n=5, **SE 0.1404, 0.72 SE from zero**, two of five seeds positive — and is
computed over the same starved bin. `safe_bin_wall_clamp_fraction_worst` is **0.985**, and
`clamp_ok` is explicitly a *recorded, non-gating* diagnostic.

### V3-EXQ-981a (MECH-027) — ree-worker-3, 4h34m, 3 seeds

A genuine engineering advance: **all eight repairs** the 2026-09-03 autopsy demanded were
implemented, including the specific inverted-band check it required of the author. Its other three
unmet preconditions now pass. Gate A aborted before Stage B, so C1 and C2 are `measured: null`.

---

## 4. Corrections to the drivers' own self-routes

Both stand, and both were independently confirmed well-founded at the red-team pass.

1. **H-env-band-absent, stamped `eliminated`** — on a coverage count taken on the **control** arms
   (31 ticks) while the **agent** gate failed at 3 in the same run, with the wall-clamp diagnostic
   that explains why excluded from the gate. **Narrowed, not eliminated.**
2. **H-avoidance-untrained, stamped `supported`** — on the 0.72-SE statistic above. **Not
   supported, and now counter-indicated** by the above-null result.

**And a third correction, to this artifact's own first draft.** The readout repair is real but was
oversold. `oracle_null_separation` is **near-tautological**: the conditional oracle sets
`held_idx = avoidant` while the measure asks whether `held_idx == avoidant`, giving ≈ 1 − 2/A ≈ 0.6
analytically against a 0.20 floor. It cannot fail for any agent-attributable reason. And "999's
oracle scored 0.0000" set an *unconditional* oracle against 999a's *conditional* one — the
predecessor's own artifact already recorded +0.905 for a conditional avoider. The elimination of
H-readout-invalid therefore rests on the **agent-above-null** result, not on the oracle gate.

Relatedly, 999a retained the single-argmax `_avoidant_action` inherited from V3-EXQ-981 — the DV
form 981a's own code documents as defective and replaced — so **"two independently repaired
instruments" overstated the independence**, and the cluster is framed accordingly.

---

## 5. Failure location (GOV-FAILLOC-1)

| | mechanism | measures | environment | REE |
|---|---|---|---|---|
| V3-EXQ-999a | not established | **partial** | **partial** | **false** |
| V3-EXQ-981a | not established | **not established** | established | **false** |

Net: **MIXED (measures + environment)** for 999a; **MEASURES** for 981a. Neither is REE FAILED, and
neither yields a mechanism verdict.

---

## 6. Re-derive brake

The R1–R3 count is **2** for both claims, arithmetically verified. **User-ratified disposition:
recorded honestly, but not read as a substrate ceiling** — there is no ceiling here, only a
measurement choice with a named cheap fix. `failure_autopsy_V3-EXQ-999_2026-09-04` anticipated
precisely this and left an in-artifact warning against reading a future count of 2 on MECH-161 as
ceiling evidence; that warning is engaged and upheld.

- **Refused:** a V3-EXQ-999b or V3-EXQ-981b reusing the band-contrast statistic unchanged.
- **Allowed and recommended:** a re-run with an agent-executable safe bin (999a) or a
  pre-registered, justified normalisation (981a); and separately a cheap **config-arm probe**
  enabling the already-built avoidance machinery, which no run in this family has ever done.

The probe is **recommended in this artifact only**. Per the standing rule, a failure-autopsy does
not spawn follow-on off its own not-yet-ratified finding; `/governance` chips it.

---

## 7. Routing

**`queue-experiment`** for both targets. **Substrate: AMEND `dv-dynamic-range-precondition-class`**
— which already lists both MECH-027 and MECH-161 in `unblocks_claims` — with two additions:

- a precondition must be **computable on the arm it will score** (999a's case: certified on control
  arms, failed on the agent arm, with the explanatory diagnostic non-gating);
- a precondition statistic's **normalisation must be pre-registered and justified** for the
  response-rate regime it is read in (981a's case).

A third amendment against the same entry comes from V3-EXQ-1017 in the companion artifact
(contrast-class matching). **Governance should apply all three in one pass.** Harness-layer; no
`ree_core` change implicated. `pending_retest_after_substrate`: true for MECH-161, and **not set**
for MECH-027, consistent with the 2026-09-03 decision and for the same reason — no substrate is
missing.

---

## 8. Recording provenance

V3-EXQ-981a: complete, 0 findings. V3-EXQ-999a: complete on always-core but carries
`substrate_stable_across_run: false`. **Not a mid-run substrate change** — one distinct cell hash,
so every cell ran against the same substrate. The checkout moved between execution and stamping, so
`substrate_commit` does not describe the `substrate_hash` the run used. **Reproduce from
`substrate_hash` `5fb5833649…`, not from `substrate_commit`.**

---

## 9. Learning extracted

1. **A run's verdict can hide its own positive result.** 999a is a FAIL whose metrics put the agent
   above the null at 4 of 5 levels; reading only the blocking gate inverts the finding.
2. **A coverage gate certified on control arms does not certify scorability of the agent arm**, and
   a count floor is not a scorability floor when the counted events can be no-ops.
3. **An oracle defined as taking the correct action cannot fail a test asking whether it took the
   correct action.** Useful as a coverage canary; not evidence the instrument can measure an agent.
4. **Comparing a repaired statistic to its predecessor requires the same definition on both sides.**
5. **A default-off flag is the first thing to check before proposing a build** — and the precedent
   cited must be for the thing actually claimed missing.
6. **At floor response rates, additive and multiplicative normalisation can disagree in sign.** The
   choice must be pre-registered and justified, not inherited.

---

## 10. Checks run

Step 7b mechanical pre-routing: `fire_count: 0`. Step 7c adversarial red-team: **CONTESTED**, run on
the **session model (Opus 5)** — the preferred cross-model pass on Fable failed twice with a monthly
spend limit on that model and was re-spawned once without the override per the skill, so this is a
**same-model** pass. Independent recomputation reproduced every load-bearing figure, and every
prose absolute tested held.
