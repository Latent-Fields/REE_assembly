# INV-051 MEL dose-sweep falsifier — actionability determination

**Status: AWAITING USER / GOVERNANCE REVIEW. Nothing in this file has been written to claims.yaml, experiment_queue.json, manual_proposals.v1.json, or experiment_proposals.v1.json. No experiment was queued.**

- **Chip:** `chip-20260808-inv051-mel-dose-sweep` (headless metaworker)
- **Generated:** 2026-08-08T12:46Z
- **Trigger:** A 2026-08-08 `/thought-digestion` pass drafted a `what_would_answer` falsifier for **INV-051** (the MEL "Goldilocks" optimal-range invariant) requiring a **>=3-level graded MEL-dose sweep** with a pre-registered rigidity DV tracing an **inverted-U**, and flagged (in the claim notes) that it was "close enough to testable-now that a dedicated chip was spawned same-day to check whether this experiment design should be registered via `/queue-experiment`."
- **This chip's finding, in one line:** **NOT queued — the inverted-U falsifier as drafted is not cleanly buildable on the current substrate.** The producer/consumer pieces are built and validated, but the substrate implements *homeostatic compensation* (more MEL → more sleep), which is the **opposite** of the *overload/decompensation* the inverted-U's upper bound requires. The upper limb of the U has **no substrate instantiation**. Running the falsifier as drafted would very likely yield a **vacuous/misleading FALSIFICATION**.

---

## 1. What the digestion pass got right

All of these are confirmed accurate:

- **SD-017** — stable (promoted provisional→stable 2026-04-24).
- **SD-MEL-PRODUCER graded knob** — built and **validated**. V3-EXQ-798a (run `...20260729T125858Z_v3`) is a clean **PASS** (`producer_validated_graded_learnable`), autopsy-confirmed (`failure_autopsy_V3-EXQ-798a_2026-07-30`, status confirmed): C1 grading 2/3 (monotone NONE<LOW<MED<HIGH), C2 above-reference 2/3, C3 sustained non-convergence 3/3, C4 learnability PASS. The old 2026-07-08 "ecological producer link broken / re-park" gate on INV-050 was formally **superseded 2026-08-01** (INV-050 `epistemic_category` graduated `substrate_ceiling → standard`).
  - *(Note the `evidence/experiments/` tree also carries a later `...20260730T010651Z_v3` 798a manifest that is a FAIL/`non_contributory`. The autopsy-confirmed canonical result is the 07-29 PASS; do not read the 07-30 artifact as the producer verdict.)*
- **SD-MEL-CONSUMER** — built and validated (`ree_core/sleep/mel_consumer.py`; C3 injection positive control in V3-EXQ-718a proved graded MEL → exact-monotone graded offline duration `[9,13,18,24,30,38]`).
- **Rigidity-proxy DVs** — `action_bias_div`, `slot_diversity`, `slot_cosine_sim`, `pred_loss`-on-novel-probe are all already instrumented and exercised in prior sleep-cluster experiments.
- **The gap is real:** no run to date (V3-EXQ-845/861/861a) has used more than a binary high-vs-low MEL contrast, and all three share the identical CausalGridWorldV2 instance and identical seeds (42/123/456). Per `claim_evidence.v1.json`, INV-051 has `genuine_exp_count: 0`.

## 2. The decisive thing the digestion pass missed — the upper bound has no substrate

INV-051 asserts an **inverted-U**: rigidity elevated at **both** extremes.

- **Lower bound** — under-stimulation (extreme monotony): learning drive under-activated → model rigidity *even when sleep architecture is intact*.
- **Upper bound** — overload (acute trauma/crisis): MEL exceeds overnight update capacity → incomplete update accumulates; *and* "MEL is rising while sleep capacity is falling" (hyperarousal, MECH-178), a **compounding deficit / decompensation**.

The just-drafted falsifier's **CONFIRMING** clause therefore requires an arm where rigidity is elevated because of **"MEL exceeding consumer clearance capacity."** The substrate cannot produce that arm:

- **The consumer models compensation, not overload.** `mel_consumer.py`:
  `factor = clamp(1 + mel_gain*(mel/ref - 1), factor_min=0.5, factor_max=3.0)`.
  Higher MEL buys **proportionally more** offline duration (more SWS/REM writes) up to a **3.0×** cap. In this substrate, more MEL → *more* processing capacity, which *completes* update better. This is the exact **opposite** of the upper-bound mechanism ("sleep capacity falling as MEL rises").
- **Ecological MEL never even binds the clamp.** The producer's learnable HIGH arm yields duration factor **~1.27** (INV-050 notes: NONE 0.885 / LOW 0.822 / MED 1.263 / HIGH 1.266) — less than half of `factor_max=3.0`. There is large unused offline headroom at ecological HIGH, so update is always well-matched by (unclamped) capacity. No overload is reachable ecologically. (Pushing the producer harder only adds *noise*-level MEL, which the 798a validation explicitly controls out as unlearnable.)
- **The one route to the clamp is injection, which is tautological.** An injected-MEL sweep can drive the factor to 3.0 (C3 reached 2.5 at injected MEL 2.5), but (a) INV-050's own documented lesson (`failure_autopsy_V3-EXQ-718a_2026-07-08`, re-derive brake **FIRED**) is that an injected/consumer sweep "would only re-demonstrate the clamp min/max by construction (tautology of `factor_min`/`factor_max`), NOT empirical evidence for the ecological invariant"; and (b) hitting `factor_max` gives the **longest** offline duration — maximal processing — not incomplete update, so it does not even instantiate overload in the required direction.
- **The genuine upper-bound mechanism is substrate-absent.** Overload/decompensation requires sleep capacity to **fall** as MEL rises — the MECH-178 noradrenergic/cortisol/LC hyperarousal coupling. `ree_core` has **no** NA/arousal control plane (MECH-178 substrate-blocked). The falsifier's own "OUT OF SCOPE" note concedes MECH-178 is absent but assumes a "simple demand-exceeds-fixed-ceiling" overload can substitute — **it cannot**, because the substrate has no fixed processing ceiling distinct from the (compensatory) duration factor, and the ecological producer cannot approach even that duration clamp.

## 3. Why queuing it as-drafted would be actively misleading

The falsifier can access only the **descending limb** of the U (under-stimulation → optimal: NONE/LOW/MED/HIGH, rigidity expected to *decrease* as MEL rises toward optimal). It cannot instantiate the ascending (overload) limb. A run over the accessible range would therefore show **monotone-decreasing rigidity** — which the drafted falsifier explicitly labels **FALSIFYING** ("rigidity is MONOTONIC in MEL-dose ... rather than U-shaped"). That would be a **false falsification**: the upper limb was never instantiated, not empirically absent. This is precisely the vacuous-FAIL / surface-a-construction-as-a-finding anti-pattern the codebase repeatedly warns against (cf. `reference_claim_synthesis_measurement_entanglement_is_debt`; the same brake that FIRED on the INV-050 718a re-grade).

Debt vocabulary: this is **`mystery (known data)`** — the probe that would have been `complex (probe-gated)` (does the producer make a graded gradient?) has **already been run** (798a PASS). What remains is a **reframe**, not a build.

## 4. Corroborating state

- Existing gated proposal for this claim: **`EXP-0376`** in `experiment_proposals.v1.json`, `status: blocked_substrate`. Its release_condition names two gates: (i) a NEW non-converging graded-MEL environment (NOT a CausalGridWorldV2 re-grade), and (ii) the MECH-178 arousal plane. Gate (i)'s *producer* half is now partially satisfied (798a validated the graded knob), but **gate (ii) — the arousal plane that instantiates the upper bound — remains unmet**, and that is the load-bearing gate for the inverted-U.
- INV-050 sibling governance (**GFLAG-0002**, user-confirmed HOLD 2026-08-07): even the *monotone* ecological coupling is held at `candidate` because 845/861/861a are **pseudo-replication** (one config × one seed set). Any future INV-051 run must additionally satisfy the independence requirement: **new seeds (not 42/123/456), and/or a held-out environment, and/or a consumer-absent control arm.**

## 5. Recommended disposition (for a `/governance` or `/thought-digestion` session — NOT chipped further, per this chip's brief)

Pick one:

- **(A) Keep INV-051 `substrate_conditional`, pending the upper-bound mechanism.** The full inverted-U falsifier is not buildable until a substrate exists in which offline update capacity **falls** (or fails to keep pace) as MEL rises — i.e. the MECH-178 arousal/decompensation plane, or an explicit fixed offline-processing ceiling the ecological producer can exceed. Neither is a simple build. This is the conservative, evidence-consistent option and matches `EXP-0376`'s standing `blocked_substrate`.
- **(B) Reframe INV-051's falsifier to a lower-bound-only test** (rigidity elevated at under-stimulation vs optimal, *with full SWS/REM cycling confirmed* to isolate it from ordinary sleep-deprivation/under-training), with a PASS/FAIL that does **not** require the inaccessible upper limb, and using genuinely independent seeds/environment per GFLAG-0002. This IS buildable now — but it tests only half the claim, is close to "less input → less learning" unless the intact-sleep dissociation is carefully instrumented, and rescoping a `candidate`/`substrate_conditional` invariant's falsifier is a governance decision, so it was **not** unilaterally queued here.

Either way, the falsifier's premise line in `claims.yaml` (`SD-MEL-PRODUCER (built, graded knob validated)`) is accurate for the *producer knob* but should be annotated that the **consumer clamp is not ecologically saturable and models compensation, not overload** — that is the operative limit, and it is what makes the drafted inverted-U falsifier substrate-conditional rather than testable-now.

---

*Author: headless metaworker session `metaworker-chip-20260808-inv051-mel-dose-sweep`. Committed under its own TASK_CLAIMS entry.*
