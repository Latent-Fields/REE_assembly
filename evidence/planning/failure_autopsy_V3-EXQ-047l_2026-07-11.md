# Failure Autopsy -- V3-EXQ-047l (MECH-095 TPJ agency-routing retest on SD-047)

- **Generated (UTC):** 2026-07-11T19:23:22Z
- **Scope:** single
- **Status:** confirmed (interactive gate answered)
- **Target:** run_id `v3_exq_047l_mech095_agency_routing_sd047_20260711T143819Z_v3`, queue_id `V3-EXQ-047l`, machine `ree-cloud-1`
- **Claim:** MECH-095 (`tpj.agency_detection_comparator`) -- candidate / substrate_ceiling / pending_retest_after_substrate
- **Verdict adjudicated:** FAIL (3/5), `non_degenerate: false`. Self-stamped `evidence_direction: mixed`; self-route decision `ceiling_confirmed_route_autopsy`.
- **Autopsy verdict:** **non_contributory** -- measurement/test-design degeneracy (empty eval negative class). The MECH-095 comparator was never exercised. **NOT a substrate_ceiling hit.**

---

## 1. Facts (from manifest -- no interpretation)

Pre-registered criteria (identical to the EXQ-047k PASS):

| Criterion | Result | Value |
|---|---|---|
| C1: contact_recall_world_routed > 0.55 | **FAIL** | 0.000 |
| C2: recall improvement (routed - baseline) > 0.04 | **FAIL** | +0.000 |
| C3: action_dissoc_mean > -0.05 | PASS | -0.004 (std 0.020) |
| C4: n_contact_probe (min) >= 20 | PASS | 105 |
| C5: no fatal errors | PASS | -- |

Load-bearing observations:

- `contact_recall_world` **and** `contact_recall_self` = **0.000 in all 8 cells** (4 seeds x ROUTED/BASELINE).
- In **every** cell `n_probe_steps == n_contact_probe` (e.g. 126==126, 119==119, 113==113, 105==105) -> the no-contact (negative) class was **empty**.
- `non_degenerate: false`; `degeneracy_reason: "contact_recall_world: zero spread (constant=0, spread=0<=eps=1e-09)"`.
- Routing head **active**: mean_routing_loss 0.0046 (ROUTED), 0.0 (BASELINE). SD-047 active: train_env_event_ticks ~4405-4484 per cell.
- Failed criterion type: **discrimination** (C1/C2). Negative-control/absolute criteria (C3/C4/C5) all pass -- but here that is not the substrate-ceiling fingerprint; it is the empty-negative-class fingerprint (see Section 3).

## 2. Claim-layer mapping

MECH-095: `mechanism_hypothesis`, status `candidate`, `implementation_phase: v3`, `epistemic_category: substrate_ceiling`, `depends_on: [SD-005, MECH-069, ARC-021]`, `pending_retest_after_substrate: true`. Lit strong (lit_conf ~0.907: Blakemore 2002, Gu 2008, Pitcher & Ungerleider 2021, Rolls 2023). EXQ-047k PASSed 5/5 on the thin CausalGridWorldV2 (contact_recall_routed 0.796, recall_improvement +0.065, n_contact_min 164). GOV-CEIL-1 floored active->candidate on 2026-07-11 with `n_ceiling_hits=0`; the SD-047 positive-discrimination retest was the owed action.

**Did the experiment test the claim under conditions where it could express itself? No.** The evaluation probe's contact-vs-no-contact partition was degenerate (empty negative class), so z_world's contact encoding was never measured against any contrast. The claim is neither supported nor weakened. `claim_ids` accuracy: correct (MECH-095 only; SD-005 dropped at queue time).

## 3. Root cause -- dispositive

The probe partition on 047l line 422:

```
is_contact = (ttype in CONTACT_SET) or (env_events > 0)
```

`multi_source_n_env_events` is a **per-step** counter (causal_grid_world.py:2292 resets it each step) incremented by env-caused hazards + transient appearances/disappearances + background-drift moves (lines 2303, 2324-2326). On SD-047 at intensity_scale=1.0 the drift/transient sources fire on essentially every step, so `env_events > 0` is true on ~every probe step -> `is_contact` true everywhere -> the no-contact class collects **zero** samples. The gate `if n_contact_probe >= 5 and len(probe_self_no_contact) >= 5` is then False, the recall block is skipped, and `contact_recall_world` keeps its init value 0.0 in every cell.

**Proof by contrast with the 047k PASS (same grid: size=12, 4 hazards, identical proximity fields):**

| | contact partition | env-events fold | n_contact_min | recall_routed | negative class |
|---|---|---|---|---|---|
| 047k (PASS, thin env) | `ttype in (hazard_approach, agent_caused_hazard, env_caused_hazard)` | **none** | 164 | 0.796 | populated |
| 047l (FAIL, SD-047) | `ttype in CONTACT_SET **or env_events>0**` | added | 105-126 (== n_probe) | 0.000 | **empty** |

The only change that saturated the partition is the added `or env_events > 0`. That fold is correct and necessary in the **training routing label** (`is_world`, 047l line 294 -- it is what makes ROUTED differ from BASELINE on SD-047) but was over-applied into the **evaluation partition**, collapsing the eval contrast.

This is the **V3-EXQ-642 pattern**: the run self-routes toward "ceiling confirmed," but the precondition for a valid test (a well-posed balanced probe with a non-empty negative class) was never met. The correct route is **re-queue, not enrichment, and not a ceiling hit** -- the SD-047 substrate ceiling has still never been validly exercised.

## 4. Biological-reference triage

Closest reference: temporoparietal junction as an agency-detection comparator (self- vs other-caused change against a textured causal background). REE's operationalisation -- a learned CE routing head trained (BCE) to predict world-vs-self causation from z_world -- is a **functional translation, not a formal-definition import** (no Pearl/Shannon/optimal-control import). The failure does **not** resemble a missing biological dependency, and it is **not** a biology divergence: it is a measurement artifact. Lit is already strong (lit_conf ~0.907), so **no `/lit-pull` commission is owed.**

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test never let MECH-095 express itself; neither supports nor weakens |
| Biological reference | clear | TPJ agency comparator; functional translation; failure is not a biology divergence |
| Prerequisites | present | SD-005 split-latent active; SD-047 landed and active |
| Implementation | complete | routing head active (route_loss 0.0046); agent trained; only the eval probe was ill-posed |
| Environment | adequate | SD-047 active (env_ev_ticks ~4470); the label, not the env, is the fault |
| **Measurement** | **misleading (dominant layer)** | env-events fold saturated `is_contact` -> empty negative class -> contact_recall_world pinned at 0.0 in all cells |
| Integration | isolated | single-mechanism probe; n/a |
| Scale | adequate | 105-126 contacts x 4 seeds; ample if the partition were well-posed |

**Dominant diagnosis layer:** measurement adequacy (test-design degeneracy / precondition-unmet). **Recommended epistemic_category for the run: `measurement_degeneracy`** -- explicitly **not** `substrate_ceiling`. MECH-095's claim-level `epistemic_category` stays `substrate_ceiling` (its mapped-to-SD-047 category); `n_ceiling_hits` stays 0.

## 6. Interpretable signals (contributory, not vacuous)

1. **Methodological (primary):** an additive label fold that is necessary in a *training* signal must not be mirrored into the *evaluation* partition -- on a dense substrate it saturates the eval class and makes the probe vacuous. Reusable lesson; drives the 047m fix and a probe-side non-degeneracy guard.
2. **Secondary, genuinely non-degenerate:** routing collapsed the self-vs-world action dissociation (BASELINE +0.101..+0.230 -> ROUTED ~0.000, i.e. z_world became about as action-predictive as z_self). Real but **claim-orthogonal** -- MECH-095 predicts world-vs-self *causation* encoding (contact recall), not action predictability. Mild hint that the routing head injects generic transition/action structure into z_world rather than cleanly isolating world-causation. Carry into 047m interpretation; do not over-read.

## 7. Learning extracted + repair pathway

Learning:
- **Measurement gap discovered:** the env-events additive fold belongs in the training routing label only, not the probe partition; on SD-047 it collapses the negative class.
- The owed SD-047 positive-discrimination retest of MECH-095 **has still not validly run.** 047l does not count as a ceiling test.
- Secondary claim-orthogonal effect (routing reduces action dissociation) noted for follow-up interpretation.

**Node classification (work_graph_debt_vocabulary):** the residual unknown -- does the SD-047-enriched routed z_world discriminate world-caused contact -- is `complex (probe-gated) / puzzle (known rules)`: the frame is well-posed and the missing item is a single fact a well-posed probe would yield. The fix to the probe itself is `complicated (buildable)`. Exactly one live hypothesis to resolve -> no fan-out.

**Routing: `/queue-experiment` -> V3-EXQ-047m** (same scientific question -> alphabetic suffix; implementation fix). Spec:
1. Keep the env-events fold in the **training** `is_world` routing label (unchanged -- necessary for ROUTED != BASELINE on SD-047).
2. Revert the **probe** `is_contact` to 047k's non-folded `CONTACT_SET` (`ttype in {hazard_approach, agent_caused_hazard, env_caused_hazard}`) -- the partition that gave n_contact_min=164 + populated negatives on the same grid.
3. **Add a probe-partition non-degeneracy guard:** require n_no_contact >= ~20 per arm; if unmet, self-route `non_contributory` (substrate/test-bed-not-ready) rather than emitting a spurious 0.0.
4. Report the secondary action-dissociation collapse alongside the recall result.

Not substrate build, not demotion, not lit-pull.

**Re-derive brake (MOVE-3):** does **not** fire. Prior substrate_ceiling/non_contributory failure_autopsy_*.json for MECH-095 = 0; this is the first, threshold = 2. Note: this autopsy's `non_contributory` reading will register as 1 in the brake's generic tally -- but it is an **instrument failure, not a ceiling confirmation.** If V3-EXQ-047m (corrected probe) **also** returns non_contributory, that is where the brake's spirit engages: two non-informative reads would implicate the operationalisation itself (not one probe bug), and governance should then route to substrate/test-bed work rather than a third 047 letter.

## 8. Interactive gate -- resolved

User confirmed (2026-07-11):
- **Routing:** Re-queue 047m (test-design fix). [047k proves a populated negative class exists on this grid.]
- **Ledger:** non_contributory, **NOT** a ceiling hit. `n_ceiling_hits` stays 0; MECH-095 stays candidate / substrate_ceiling / pending_retest_after_substrate.

## 9. Draft `evidence_quality_note` (for `/governance` to write -- NOT written by this skill)

> V3-EXQ-047l (2026-07-11, SD-047 retest, 4 seeds, ree-cloud-1) FAILed 3/5 but is NON_CONTRIBUTORY, not a ceiling confirmation. The probe's contact-vs-no-contact partition saturated: `is_contact` folded `env_events>0`, which on SD-047's dense per-step drift/transient dynamics was true on every probe step, so the no-contact negative class was empty (n_contact == n_probe in all 8 cells) and contact_recall_world was structurally pinned at 0.0 in BOTH ROUTED and BASELINE. The MECH-095 agency comparator was never exercised. Root cause: the `or env_events>0` fold over-applied to the probe partition (correct only in the training is_world routing label). The owed SD-047 positive-discrimination retest therefore STILL has not validly run; n_ceiling_hits stays 0 (measurement degeneracy, not a substrate_ceiling hit). Re-queued as V3-EXQ-047m (keep the fold in the training label; revert probe is_contact to 047k's non-folded CONTACT_SET, which gave n_contact_min=164 + recall 0.796 on the same grid; add a probe-partition non-degeneracy guard). MECH-095 stays candidate / substrate_ceiling / pending_retest_after_substrate. Secondary non-degenerate signal: routing collapsed the self-vs-world action dissociation (BASELINE +0.10..+0.23 -> ROUTED ~0) -- real but claim-orthogonal; carry into 047m interpretation.

Governance actions implied (this skill does not apply them):
- Set `evidence_direction: non_contributory` + note on the 047l manifest (flat + runs/ pack); rebuild indexes; mark reviewed in review_tracker.json; regenerate pending_review.py to confirm 0 pending for 047l.
- MECH-095: append the note above; **no status/category change**; keep `n_ceiling_hits=0` and `pending_retest_after_substrate: true`.
