# Claim Synthesis -- SD-034 commitment-closure-control-plane cluster (de-commit-authority granularity-debt decomposition)

- **Generated:** 2026-06-19T20:34:22Z
- **Status:** PROPOSAL (proposal-first; nothing registered without per-child user approval)
- **Routed by:** confirmed `failure_autopsy_V3-EXQ-460g_2026-06-19` (PRIMARY action, user-adjudicated 2026-06-19). The 460f autopsy WATCH ITEM pre-registered this exact trigger; it fired on 460g.
- **Cluster:** SD-034 ClosureOperator behavioural de-commit authority over the MECH-090 beta latch -- 7 autopsies (2026-06-04 .. 2026-06-19).
- **Concurrency note:** an active `/governance` session (`governance-cycle-20260619T2013Z`, claimed 2026-06-19T20:13Z) holds the governance collision set (`claims.yaml`, `claims.json`, `substrate_queue.json`). This proposal touches NONE of those files. Registration (Step 7) is gated on (a) per-child user approval AND (b) that governance session releasing the collision set.

---

## 0. One-line verdict

The cluster **clears the granularity-debt bar** (Step 3 PROCEED): >=2 distinct, genuine, non-degenerate, **substrate-ready** FAIL signatures circling one coarse claim, with positive existence proofs ruling out falsification and a built substrate ruling out substrate-not-ready. The coarse claim "the SD-034 ClosureOperator has behavioural de-commit authority over the MECH-090 beta latch" bundles a **multi-stage de-commit pipeline** it does not name. Proposed decomposition: **SD-034 retained as the umbrella design_decision (narrowed)** + **two new mechanism_hypothesis children** that are independently testable and lit-grounded -- closure->beta **coupling engagement** and de-commit-authority **magnitude**. One candidate child is **explicitly REFUSED** by the anti-proliferation rail (coupling-measurability-under-refractory is a measurement/test-design property with no biological mechanism -- it is the 460h experiment fix, not a claim). The 460h re-queue then targets the re-grained children, not the coarse umbrella.

---

## 1. The cluster's failure record (7 autopsies)

| # | Run(s) | Date | Signature (what failed) | Step-3 class |
|---|---|---|---|---|
| 1 | 460b/461b/464b/466b/467b/468b | 06-04 | `committed_mode_curriculum` never produced goal completions; agent commits but never tolerance-completes a waypoint -> `n_closures=0` everywhere | **substrate-not-ready** (goal-achievement layer) -> routed to `scaffolded_sd054_onboarding`. EXCLUDE from the de-commit signal. |
| 2 | 460c/468c + 461c/466c | 06-12 | On the 603n foraging-competent substrate, closure done-token never fires: env `sequence_complete` not routed into `emit_closure()` AND automatic rule-stability detector unmet (untrained rule_bias_head) | **closure FIRING absent** (S1). substrate_ceiling at the time. |
| 2b | 464c/467c (mode-gov), 629b (readiness) | 06-12 | SPLIT OFF to distinct substrate gaps (mode-governance-engagement; nav-competence). Different claims/substrates. | EXCLUDE -- not the de-commit-authority cluster. |
| 3 | 460d/468d | 06-13 | Leg A+B closed `n_closures=0` (460d C1 PASS: closure now FIRES via hook). De-commit authority absent because Leg C (trained rule_bias_head) code-confirmed unbuilt (flag set, never optimized) | **detector MAGNITUDE / head training** (S2). experiment-side-unbuilt -> substrate amend. |
| 4 | 460e | 06-17 | Leg C now trains (rule_bias_trained 1.0). MECH-090 bistable latch fails to engage on 2/3 seeds (commit-without-beta dissociation: beta elevates only on natural `result.committed`, decoupled from closure-installed committed_trajectory). Self-routes before C2 DV. Seed 44 = existence proof | **closure->beta COUPLING engagement** (S3). substrate amend. |
| 5 | 460f + 468e | 06-18 | beta-engagement amend worked; C2 de-commit DV ran for the first time. PASS seed 42 (-33.5%), FAIL 43/44. Coupling fired 36/52 seed 42 but 0/0 on 43/44 -> on strong-natural-commit seeds the DV reduced to the bare 5-tick refractory, **swamped** by ~530-560 elevated steps. 468e independent DV confirms same gap (C1 release PASS 3/3, C2 committed_frac pinned at 1.0 ceiling). Seed 42 + 460e seed 44 = existence proofs of correct sign | **de-commit-authority MAGNITUDE** (S4) + DV power. substrate_ceiling + measurement. NOT a fair-test weakens. |
| 6 | 460g | 06-19 | Armed BOTH 460f-prescribed amends: (a) committed-run-scaled refractory MAGNITUDE lever + (b) tightened `sd034_n_closure_coupled_elevations > 0` non-vacuity gate. **Self-defeating in direct tension**: scaling the refractory to overcome swamping pins it at the 60-tick cap; `elevate()` is a no-op while refractory active, so the closure-coupled re-elevations the gate counts can never fire. Coupling counter 36 -> 0 on seed 42. De-commit HAS authority (seed-42 within-arm occupancy 0.333 -> 0.0) but suppresses its own certifier | **coupling MEASURABILITY under refractory** (S5). measurement/test-design entanglement ON TOP OF granularity-debt recurrence. |

**The five de-commit-pipeline sub-signatures that circle SD-034 (excluding the upstream-substrate and split-off siblings):**

- **S1 closure FIRING** (460c/d) -- does the completion event emit a closure?
- **S2 detector MAGNITUDE / trained head** (460d/e) -- is the rule_state magnitude-bearing so the automatic detector can fire?
- **S3 closure->beta COUPLING engagement** (460e/f) -- does the closure-plane commit actually elevate/bind the latch (distinct from natural commit-entry)?
- **S4 de-commit-authority MAGNITUDE** (460f/468e) -- is the post-closure refractory strong enough to overcome natural-commit latch occupancy?
- **S5 coupling MEASURABILITY under refractory** (460g) -- can the de-commit be certified when a strong-enough refractory suppresses the coupling-coupled elevation the DV counts?

---

## 2. Discrimination gate (Step 3 -- the load-bearing filter)

Classifying the de-commit cluster (S1-S5) against the four Step-3 classes:

**(a) vacuous-criterion / test-design debt? -- NO (the dangerous re-read, addressed head-on).**
The 460g reading is "measurement/test-design entanglement," and S4/S5 involve measurement, so the gate demands we check whether this is really the MECH-341 `660 -> 660a -> 660b` pattern (same test iterated, `claim_alignment: NOT weakened` + below-resolution, fix/retire the test). It is **not**, for three reasons:
1. **Five structurally-DIFFERENT signatures**, not one test iterated three times below resolution. The MECH-341 STOP case was the *same* graded-in-K falsifier re-run; here each retest probes a *different link* in the chain.
2. The measurement entanglement in S5 is **caused by the interaction of the two mechanisms under test** (the de-commit refractory and its coupling certifier ride the same `_refractory_remaining` window; `elevate()` is a no-op during it). That interaction *is* the missing structure the coarse claim does not name -- it is granularity debt surfacing *as* a measurement fault, not a low-resolution readout on an unchanged test. (Contrast 514m `C_WL=0.0` on a never-written channel / 642 `z_block` identically 0 on an untrained encoder -- those are vacuous *by construction independent of behaviour*; 460g's vacuity is *produced by the lever under test*.)
3. The autopsies tracked this explicitly: 460c/460e/460f all read the recurrence as **link-by-link escalation, NOT granularity debt**. The 7th (460g) tipped it -- the 460f WATCH ITEM fired -- because the count (7) + the now **mutually-tensioned levers** (fixing magnitude breaks the coupling metric) is the tell that the single "de-commit authority" property bundles separable, *interacting* mechanisms. User-adjudicated 2026-06-19.

**(b) substrate-not-ready? -- NO (anymore).** S1/S2/S3 were substrate-readiness on the way up, but the substrate is now **fully built**: Legs A (env-completion hook) + B (de-commit refractory) + C (trained rule_bias_head) + beta-coupling + committed-run-scaled magnitude lever ALL landed and firing. The 460g autopsy: "not substrate_ceiling (the substrate carries and expresses the de-commit on seed 42)." We are past the wait-for-substrate class.

**(c) clean single-point falsification? -- NO.** Seed-42 within-arm de-commit (occupancy 0.333 -> 0.0, 460g) is a **positive existence proof** that de-commit authority exists. Seed-44 (460e, ON 11.73 < OFF 14.87) and seed-42 (460f, -33.5%) confirm the correct sign. The claim is not wrong; it is coarse. Decomposing a wrong claim does not rescue it -- but this claim is underspecified, not false.

**(d) granularity debt (the residue)? -- YES. PROCEED.** >=2 distinct, genuine, non-degenerate, substrate-ready FAIL signatures circling SD-034: we have five (S1-S5), of which at minimum **S3 and S4 are genuine, on the built substrate, and dissociate from each other** -- the decisive evidence:

> **The dissociation is the proof they are separate mechanisms.** 460f: coupling ENGAGES (seed 42: 36 coupled elevations) yet magnitude is INSUFFICIENT (swamped). 460g: magnitude HAS authority (seed 42: 0.333 -> 0.0) yet coupling is UNMEASURABLE (counter 0). Coupling-without-authority and authority-without-measurable-coupling are double-dissociated across two runs. A single "de-commit authority" property cannot express that dissociation; two named children can.

**STOP test:** does the cluster survive after filtering? Yes -- S3 (coupling engagement) and S4 (de-commit magnitude) are the granularity-debt residue. S1 is essentially closed (closure fires via hook). S2 is a built leg. S5 is the measurement-entanglement half routed to the 460h fix (NOT a claim -- see Section 4).

---

## 3. The common thread (Step 4)

> **Every failure is a distinct broken (or unmeasurable) link in the closure -> latch de-commit *pipeline* -- closure-firing, closure->latch coupling, de-commit magnitude, and de-commit-measurability-independent-of-the-lever -- which the single "de-commit authority" claim collapses into one undifferentiated property. The chain also reveals that two of those links (the magnitude lever and the coupling certifier) interact destructively because they share the same refractory control-state -- a structural fact the coarse claim cannot represent.**

The coarse SD-034 de-commit clause treats "behavioural de-commit authority over MECH-090" as one property. The 7-autopsy chain shows it is a **sequence of separately-failing, separately-testable couplings**, with a cross-link interaction at the magnitude/measurement boundary.

---

## 4. Lit grounding (Step 5)

The SD-034 lit-pull exists: `evidence/literature/targeted_review_sd_034/entries/` -- 6 entries (Rich & Shapiro 2009 strategy-switch; Schuck 2016 OFC state-map; Collins & Frank 2014 OPAL task-set disengagement; Mayr & Keele 2000 backward inhibition; Smith & Graybiel 2013 dual-operator bracketing; Barnes 2011 task-bracketing). The 460g autopsy records `lit_status: present`, `is_formal_import: false` -- the closure mechanism class is a faithful biological translation, not a formal import. No NEW full `/lit-pull` is required at the mechanism level; the decomposition stays within the already-vetted biological frame. Per-child grounding:

| Proposed child | Biological anchor (existing SD-034 lit-pull) | Adequacy |
|---|---|---|
| **Child A -- closure->beta coupling engagement** | Collins & Frank 2014 (OPAL D1/D2 task-set disengagement -- completion drives the committed program OFF); Smith & Graybiel 2013 (the "stop" bracket terminates the action sequence) | **Adequate.** Completion-triggered disengagement of the committed motor program is the coupling. |
| **Child B -- de-commit-authority magnitude** | Mayr & Keele 2000 (backward inhibition: post-completion refractory whose *strength* competes with re-activation of the just-abandoned set); Cisek & Kalaska 2010 / Cavanagh & Frank 2011 (STN conflict-graded release -- the brake magnitude scales with re-commitment pressure; both cited in the cluster autopsies) | **Adequate via Mayr & Keele.** Cavanagh & Frank 2011 (STN "hold-your-horses" graded release) is the *sharpest* anchor for the "magnitude scales with committed-run length" form but is **not yet a formal entry** in the SD-034 lit dir. RECOMMEND a targeted single-entry addition at registration time (not a blocker; the magnitude form is already grounded by Mayr & Keele's strength-competes-with-reactivation finding). |

**Refused-child lit check:** the would-be child "coupling-measurability-under-refractory" has **no biological mechanism to ground** -- it is an instrumentation property (count commit INTENTS before the elevate/refractory gate). The "biology before formal definitions" discipline means it must NOT be registered as a claim. It is routed to the 460h experiment design (Section 6).

---

## 5. The decomposition PROPOSAL (Step 6)

### 5.1 Fate of the coarse claim

**SD-034 -> UMBRELLA (narrowed-and-retained).** SD-034 stays a `design_decision` asserting the ClosureOperator EXISTS, fires the five-part "done" token, and that closure firing + No-Go install are demonstrated (460d C1 PASS, MECH-260 supports). The **de-commit-authority sub-clause is decomposed out** into named children. SD-034 is NOT demoted (positive existence proofs; provisional holds) and NOT superseded (the operator and its firing are real). The de-commit clause in the SD-034 title becomes "the de-commit pipeline (coupling + magnitude) is decomposed into MECH-44X / MECH-44Y; see children."

### 5.2 Proposed children (each independently testable)

**Proposed ids: next free at registration time** (current max `MECH-444`; concurrent sessions hold the governance set, so re-check max + recent `git log` at write time. Provisionally MECH-445 / MECH-446.)

---

#### Child A -- closure->beta coupling engagement

- **proposed id:** MECH-445 (next free at registration)
- **claim_type:** mechanism_hypothesis
- **subject:** governance.closure_beta_coupling
- **polarity:** asserts
- **status:** candidate
- **epistemic_category:** standard (V3-tractable; the substrate is built; testable once the 460h refractory-independent metric lands)
- **implementation_phase:** v3 ; **v3_pending:** true ; **pending_retest_after_substrate:** true (commitment-closure-control-plane)
- **one-line claim:** "A closure-plane commit (closure fired on a real sequence completion) elevates/binds the MECH-090 bistable latch via the `use_closure_commit_beta_coupling` path **independent of a natural `running_variance < commit_threshold` commit-entry** -- i.e. on seeds where the agent does not naturally commit decisively, the closure still drives a latch elevation the de-commit then acts on."
- **what_would_answer:** "On the foraging-competent 603n substrate with the beta-coupling amend ON, a **refractory-independent commit-intent counter** (closure-plane `e3._committed_trajectory` forming while `not result.committed`, counted BEFORE the elevate/refractory gate) is `> 0` on >= 2/3 scored seeds, including a strong-natural-commit seed. Falsified if the closure-plane commit only ever co-occurs with a natural `result.committed` (coupling inert -- adds no elevation the natural path would not have produced) on >= 2/3 seeds."
- **depends_on:** SD-034 (umbrella), MECH-090 (the latch it engages), SD-033a (rule_state the closure reads)
- **lit anchor:** Collins & Frank 2014; Smith & Graybiel 2013 (SD-034 lit-pull)
- **cluster evidence it explains:** 460e (commit-without-beta dissociation, beta engaged 1/3); 460f (coupling fired 36/52 seed 42 but 0/0 on 43/44 -- engagement is seed-conditional). The seed-42 coupling (460f) is partial positive support; the 43/44 inertness is the open failure.
- **why distinct from B:** coupling can engage with insufficient magnitude (460f seed 42).

---

#### Child B -- de-commit-authority magnitude

- **proposed id:** MECH-446 (next free at registration)
- **claim_type:** mechanism_hypothesis
- **subject:** governance.closure_decommit_magnitude
- **polarity:** asserts
- **status:** candidate
- **epistemic_category:** standard (V3-tractable; substrate built; testable on the 460h within-arm DV)
- **implementation_phase:** v3 ; **v3_pending:** true ; **pending_retest_after_substrate:** true (commitment-closure-control-plane)
- **one-line claim:** "The closure-coupled de-commit lowers post-closure latch occupancy with **authority magnitude sufficient to overcome the natural-commit occupancy it competes against** -- the committed-run-scaled refractory drives a within-arm around-closure occupancy drop (pre-closure vs post-closure window on the ON arm), scaling with committed-run length so a long committed run triggers a proportionally long de-commit."
- **what_would_answer:** "On the amended substrate (committed-run-scaled refractory ON), the ON-arm **within-arm** post-closure latch occupancy is below the pre-closure occupancy by >= `DECOMMIT_MIN_DROP_FRAC` on >= 2/3 seeds, measured on a **refractory-independent coupling gate** (so the lever does not zero its own certifier). Falsified if a fairly-coupled, refractory-independent-gated run shows no within-arm post-closure drop (the de-commit fires with correct sign but sub-threshold authority) on >= 2/3 seeds."
- **depends_on:** SD-034 (umbrella), MECH-090 (the latch occupancy), MECH-445 (coupling must engage for the magnitude to act on a closure-driven elevation), MECH-342 (maintenance-release sibling -- the *other* release pathway; cross-ref to keep the boundary clean)
- **lit anchor:** Mayr & Keele 2000 (post-completion refractory strength); Cavanagh & Frank 2011 (STN graded release -- targeted lit addition recommended)
- **cluster evidence it explains:** 460f (5-tick refractory swamped by ~530-560 elevated steps -- correct sign, sub-threshold magnitude); 468e (release fires C1 3/3 but committed_frac pinned at 1.0 -- sub-threshold authority via an independent DV); 460g (committed-run-scaled refractory HAS authority on seed 42, 0.333 -> 0.0 -- the existence proof). 
- **why distinct from A:** magnitude can have authority with unmeasurable coupling (460g seed 42 dissociation).

### 5.3 REFUSED child (anti-proliferation rail)

**"coupling-measurability-under-refractory" -- NOT minted.** The 460g signature S5 (the strong refractory suppresses the very coupling metric the de-commit is scored by) is a **measurement / test-design property**, not a biological mechanism. It has no `what_would_answer` that falsifies a *claim about cognition* -- its resolution is an instrumentation change (count closure-plane commit INTENTS before the elevate/refractory gate, per the 460g autopsy `recommended_substrate_queue_entry`). Minting it would manufacture an untested "claim" from a measurement artefact -- exactly what the discrimination gate exists to prevent. It is handled by the **460h experiment** (Section 6), and it is *why* Children A and B both carry "refractory-independent coupling gate" in their `what_would_answer`.

### 5.4 Not minted, by design

- **closure-firing (S1):** already shown via the Leg-A env-completion hook (460d C1 PASS; MECH-260 supports). Folded into SD-034's narrowed umbrella scope, not a fresh candidate. The *automatic-detector* firing variant (n_automatic_fires=0 throughout) is **MECH-261's** mode-conditioning territory, not a new SD-034 child -- the cluster never exercised it (do not weaken the stable claim).
- **detector-magnitude / head training (S2):** a built substrate leg (scaffold_train_rule_bias_head, validated by smoke), not a standing mechanism claim. It is the *precondition* for the automatic detector, captured in the substrate, not the registry.

---

## 6. Hand-off (Step 8)

1. **460h re-queue (secondary route, GATED on this decomposition).** Per the 460g autopsy `recommended_substrate_queue_entry`: amend `commitment-closure-control-plane` with a **refractory-independent coupling counter** (increments on the closure-plane commit INTENT -- `e3._committed_trajectory` forming while `not result.committed` -- BEFORE the elevate/refractory gate), then 460h scores the within-arm around-closure occupancy drop (seed-42-style 0.333 -> 0.0) against the intent-based gate. **460h targets the re-grained children (MECH-445 coupling + MECH-446 magnitude), NOT the coarse SD-034 closure umbrella.** Acceptance: refractory-independent commit-intent counter `> 0` on >= 2/3 scored seeds AND ON within-arm post-closure occupancy `<` pre-closure by >= `DECOMMIT_MIN_DROP_FRAC` on >= 2/3 seeds. New letter; do NOT re-author 460d/e/f/g.
2. **On user approval (Step 7):** register the approved children into `claims.yaml` + arch-doc stubs in `docs/architecture/sd_034_governance_closure_operator.md` (new "Children" section), wire SD-034 umbrella `depends_on` / reverse-dep, run `python scripts/build_claims_json.py`, pathspec-limited commit + push. **Blocked until the active governance-cycle-20260619T2013Z session releases the claims.yaml/substrate_queue collision set.**
3. **Recommended targeted lit addition:** one entry for Cavanagh & Frank 2011 (STN conflict-graded release) into `evidence/literature/targeted_review_sd_034/entries/` as Child B's magnitude anchor (non-blocking).
4. **Plan node:** `commitment_closure:GAP-4` resume_condition to be refreshed (by the governance session or a later walk) to: closes when 460h returns a contributory PASS on the refractory-independent metric for the re-grained children MECH-445 + MECH-446.

---

## 7. Discipline checklist (self-audit)

- [x] Discrimination gate run; cluster classified as granularity debt **after** ruling out vacuous/test-design (the MECH-341 660-series re-read), substrate-not-ready, and clean falsification.
- [x] Every proposed child carries a `what_would_answer` (falsifier). Children without one were not proposed.
- [x] One candidate REFUSED on the anti-proliferation rail (no biological mechanism -> not a claim).
- [x] Lit-grounded (existing SD-034 pull; one targeted addition flagged, non-blocking).
- [x] Proposal-first: no `claims.yaml` / `substrate_queue` edit; per-child user approval pending; concurrency-safe (governance collision set untouched).
- [x] Generates `candidate` children only; promotion is `/governance`'s, building is `/implement-substrate`'s, testing is `/queue-experiment`'s (460h).
