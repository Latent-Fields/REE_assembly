# Failure Autopsy — INV-089 / INV-090 well-posedness (measurement-instrument reframe)

- **Generated (UTC):** 2026-07-16T06:16:57Z
- **Scope:** cluster (the INV-089/INV-090 claim family — one shared root)
- **Status:** confirmed (interactive gate answered)
- **Kind:** REFRAME pass on the measurement instrument, **not** a new failed run. Triggered at `/queue-experiment` Step 2.4 when the INV-089 ceiling-form envelope test — the move `claim_synthesis_INV-089_2026-07-16.md` §7 assigned to INV-089 — was found analytically vacuous in the current substrate before any script was written.
- **Prior autopsies on the lineage:** `failure_autopsy_morning-digest-742-744a-745-746-746a_2026-07-13`, `failure_autopsy_V3-EXQ-744_2026-07-12`, `failure_autopsy_V3-EXQ-746b_2026-07-15`, `failure_autopsy_746c-756_2026-07-16`. INV-089 carries **2** prior non_contributory/ceiling autopsies (746b, 746c); this is the **3rd**.

---

## 0. Provenance chain (how we got here)

746c (first VALID met-precondition bound test) FAILed C1/C2/C3 in a **non-binding regime** → adjudicated non_contributory (`failure_autopsy_746c-756_2026-07-16`) → routed to `/claim-synthesis` → INV-089 **split** 2026-07-16 into:
- **INV-089** (narrowed, retained) = the **CEILING**: `harm_eval quality <= f(z_harm differentiation)`.
- **INV-090** (new, candidate/substrate_conditional) = the **DRIVER**: `harm_eval quality RISES WITH differentiation` in a binding regime.

The split's hand-off (`claim_synthesis_INV-089_2026-07-16.md` §7 step 6): INV-089 → `/queue-experiment` a ceiling-form **envelope** test (no build owed); INV-090 → `/implement-substrate` a binding-regime maturation curriculum, THEN `/queue-experiment`.

This session was tasked with the INV-090 build + driver test. A worth-it **sanity-check** (user-requested, at the task gate) found the INV-090 build not worth it; on then attempting the INV-089 envelope test, a substrate read found **it** analytically vacuous too. Both findings trace to one root — hence this reframe autopsy on the whole family.

---

## 1. Facts (verified in code — no interpretation)

The 746 experiment family has **no `harm_eval` object distinct from "same-capacity decode of the harm target from z_harm."**

- `harm_eval_z_harm(z_harm)` is literally `self.harm_eval_z_harm_head(z_harm)` — a plain `Linear→ReLU→…→scalar` MLP (`ree-v3/ree_core/predictors/e3_selector.py:681`, head defined :278).
- In `v3_exq_746c` (`ree-v3/experiments/v3_exq_746c_inv089_harm_eval_z_harm_bound_target_corrected.py`):
  - **DV** ("harm_eval quality") = `_train_dv_kfold` (:375) → a **fresh-init** `harm_eval_z_harm_head` MLP trained on frozen z_harm to decode the target (`prox`), k-fold held-out R².
  - **IV** ("z_harm differentiation") = `_ridge_heldout_r2` (:255) → a **linear ridge** decode of the *same* target from the *same* frozen z_harm.
- The maturation curriculum (`experiments/_lib/baselines/maturation_curriculum.py::_mature_harm_encoder` :600) trains **only the HarmEncoder**, via a **throwaway** prox `temp_head` that is discarded. There is no separately-objective'd evaluator anywhere in the loop.
- Collected targets and their maturation behaviour (from the 746a/b/c manifests, recorded in the 746c header): `prox` already-high (~0.84 at onset 0, → ~0.88); `dens` = small-sample underfitting artifact (gradient washes out at adequate n); realized-harm **`Y` = FLAT** (~0.03–0.06, no gradient — a random-walk agent rarely experiences graded harm).

## 2. Claim-layer mapping

- **INV-089** `harm_evaluator_bounded_by_z_harm_differentiation` — invariant/emergent, **provisional**, sole undisturbed support = 743 (positive control: single-pathway z_harm decodability rises with maturation). Narrowed to the ceiling 2026-07-16.
- **INV-090** `harm_evaluator_quality_grows_with_z_harm_differentiation` — invariant/emergent, **candidate/substrate_conditional/pending_substrate_reconfirmation**, driver reading, thinner + partly counter-indicated lit warrant.

Did the (proposed) tests let the claims express themselves? **No** — for a structural reason, below. This is a measurement/claim-framing failure, **not** claim falsification. INV-089 stays provisional on 743; INV-090 stays candidate.

## 3. The well-posedness failure (the load-bearing move)

**CEILING (INV-089) is analytic, not empirically falsifiable, under this instrumentation.** "harm_eval quality" = held-out R² of a same-capacity MLP decoding the target from frozen z_harm. "same-budget z_harm→target decodability ceiling" = held-out R² of a same-capacity decoder of that target from that z_harm. **Same object.** So `harm_eval ≤ ceiling` holds *by definition* — an evaluator cannot decode the target better than the best same-capacity decode of the target; the only way to observe `harm_eval > ceiling` is estimator/split noise → `vacuous_pass` by construction.
- Escape route "ceiling = linear ridge IV": a nonlinear MLP evaluator **legitimately** beats a linear probe → yields **false falsifications** of the bound. No capacity between linear-ridge and same-capacity-MLP makes it a real bound *about differentiation*.

**DRIVER (INV-090) is welded to the ceiling.** A binding-regime curriculum, by construction, clamps differentiation as the *sole* bottleneck; the evaluator reads the same z_harm for the same target, so DV tracks IV upward by construction. A monotone-coupling PASS is *entailed* by the ceiling (the ceiling in a binding regime already predicts co-movement — see the 746c autopsy), so it does **not** discriminate the driver from the ceiling. The only discriminating FAIL (evaluator flat below a rising ceiling) is near-impossible when the representation is engineered to be the bottleneck. Lit is thinner and counter-indicated (Verriotis-Fitzgerald 2016: nociceptive maturation is non-activity-dependent), and the curriculum's supervised prox regression is itself the activity-dependent caricature that lit warns against.

**All three candidate reframes converge on one unblock — which is itself substrate-blocked:**
- (a) **Intrinsic differentiation** (eff-rank / silhouette instead of target-decodability): fails to yield a valid bound. A scalar target (`prox`) is perfectly decodable from a rank-1 z_harm, so "decode ≤ eff-rank" is not a real upper bound; class-silhouette collapses back to class-decodability (circular again).
- (b) **Distinct non-flat evaluation target** (evaluator objective ≠ representational-decodability probe): the only in-substrate candidate is realized-harm `Y`, which is **flat** → starves.
- (c) **Real in-substrate harm_eval head vs the ceiling** (the head as trained by the agent's actual ethical-cost/harm signal, not supervised target regression): the real training signal is realized harm `Y` → flat → the head does not train → starves.

The shared requirement of (b)/(c): a **non-flat, experienced harm-evaluation signal distinct from supervised prox regression**, which needs an environment with graded *experienced* harm **and a policy that commits to harm-relevant action.** That is the same committed-action / conversion (F-dominance) ceiling that blocks the behavioural program (`memory/feedback_dont_queue_commitment_dependent_behavioural.md`). So the one constructive substrate direction is `complicated (buildable)` **blocked on an already-known ceiling** — and not worth building now against INV-090's thin, counter-indicated warrant.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | INV-089 intact-but-analytic; INV-090 intact-but-untestable | measurement/framing failure, not falsification |
| Biological reference | partial / counter-indicated | Verriotis-Fitzgerald 2016 pressures the driver's experience-driven co-rise; ceiling itself is lit-grounded (0.793) but non-binding here |
| Prerequisites / substrate | present | SD-010 HarmEncoder + harm_eval_z_harm IMPLEMENTED |
| Implementation | **structurally circular** | evaluator ≡ same-capacity decoder of the same target; no independent evaluation objective |
| Environment | **inadequate** | realized-harm Y flat → no distinct non-flat evaluation signal exists |
| Measurement | **ill-posed** | `harm_eval ≤ decodability ceiling` is analytic (MLP ceiling) or false-falsifying (linear ceiling) |
| Integration | n/a | single-stream measurement |
| Scale / capacity | adequate | not a data-volume problem |

**Node class:** `complex (probe-gated) / mystery (known data)` — the 746 family already contains the data showing evaluator = its own ceiling; the FRAME is wrong. Reframe, do not gather; do not build a binding curriculum.

## 5. Re-derive brake (MOVE-3) — FIRES

INV-089 carries **2** prior non_contributory/ceiling autopsies (746b, 746c); this reframe is the **3rd** non_contributory-family reading (`RE_DERIVE_BRAKE_THRESHOLD` = 2, exceeded). The brake **FIRES**:
- A same-claim, same-granularity test re-queue is **REFUSED** — no lettered driver/ceiling iteration against the current instrumentation (this includes both a naive same-regime driver 746-letter *and* the ceiling-form envelope test, which is analytically vacuous).
- Route is **NOT** `/queue-experiment`. The only constructive direction is an `/implement-substrate` distinct-non-flat-evaluation-target build — but that is itself blocked on the commitment/conversion ceiling and is **not** recommended for creation now (see routing). So the effective route is **HOLD** (governance narrows the notes; no build, no queue).

## 6. Learning extracted

1. **A "bound" whose two sides are measured by the same estimator is analytic, not empirical.** INV-089's ceiling operationalized both "harm_eval quality" and "the decodability ceiling" as a same-capacity decode of the same target from frozen z_harm — so the bound is true by construction. An empirically testable ceiling needs the evaluator and the ceiling-decoder to be **genuinely different objects** (different objective, or genuinely different capacity in the direction that can only make the evaluator *worse*).
2. **The INV-089/INV-090 split did not resolve the wall; it re-expressed one root as two children.** Both children are blocked on the *same* missing primitive — a distinct, non-flat, experienced harm-evaluation signal — which is itself blocked on the committed-action / conversion ceiling. Splitting a claim does not create a testable instrument where none exists.
3. **`prox` being "already-high at onset 0" was never a regime problem to be engineered around** — it is a symptom that `prox` is a raw input feature the untrained encoder linearly carries, and that the family has no evaluation object distinct from decoding it. Engineering a binding regime would have manufactured a self-fulfilling co-rise, not tested a driver.
4. This is the earliest a human sees the well-posedness defect: it was caught at `/queue-experiment` Step 2.4 (before writing a script), not after a multi-hour run banked a `vacuous_pass`.

## 7. Routing (user-confirmed at gate)

- **INV-089 → NARROW-IN-PLACE, stays provisional (governance write, no run).** Reframe the `evidence_quality_note`: the same-budget-decodability ceiling is **analytic** under current instrumentation (evaluator = its own decodability ceiling), not an empirically expressible invariant; its only empirical content (decodability rises with maturation) is already carried by 743's positive control. Set `pending_retest_after_substrate: true` gated on a **distinct non-flat evaluation target**. **No demotion** — 743 remains the undisturbed support; stays provisional. `narrow_supports_flag: true` (sole support is 743's single-pathway positive control).
- **INV-090 → HOLD candidate/substrate_conditional; binding-curriculum build REFUSED (no substrate_queue entry created).** Record that the binding-regime maturation curriculum does **not** resolve the evaluator=decoder weld (it manufactures a self-fulfilling co-rise), so it is refused; the real unblock is a distinct non-flat evaluation target, itself blocked on the commitment/conversion ceiling. Keep the thin/counter-indicated-warrant caveat already in the notes. Governance may later choose to retire the driver reading if the commitment ceiling proves durable.
- **Re-derive brake:** fired; refuse same-claim re-queue; route = HOLD (not queue, not build-now).
- **No substrate_queue entry created** (`recommended_substrate_queue_entry.action = none`): the distinct-evaluation-target substrate is real but doubly blocked (flat Y + committed-policy/conversion ceiling) and thinly warranted; creating an entry now would add a `blocked_by`-on-a-blocked-ceiling node with no near-term action. Governance tracks the dependency via the INV-089/INV-090 notes instead.

## 8. Draft `evidence_quality_note`s for governance (do not write from this skill)

**Appended to INV-089 (ceiling) context:**
> 2026-07-16 (INV-089/090 well-posedness autopsy — `failure_autopsy_INV-089-INV-090-wellposedness_2026-07-16`): the ceiling-form envelope test assigned by the 2026-07-16 split is **analytically vacuous** under the 746 instrumentation. "harm_eval quality" and "the same-budget z_harm→target decodability ceiling" are the SAME measurement (a same-capacity MLP decoding the target from frozen z_harm), so `harm_eval ≤ ceiling` holds by construction and any violation is estimator noise (a linear-ridge ceiling instead yields false falsifications). The bound is therefore analytic, not an empirically expressible invariant; INV-089's only empirical content (decodability rises with maturation) is already carried by 743. No demotion — stays **provisional** on 743's single-pathway positive control (`narrow_supports_flag`). `pending_retest_after_substrate` on a **distinct non-flat harm-evaluation target** (evaluator objective ≠ representational-decodability probe); the only in-substrate candidate, realized-harm Y, is flat, so the retest is blocked on the committed-action/conversion ceiling. Re-derive brake fired (3rd non_contributory-family reading); a same-claim test re-queue is REFUSED.

**Appended to INV-090 (driver) context:**
> 2026-07-16 (INV-089/090 well-posedness autopsy): the driver reading is **welded to the ceiling** by the representation bottleneck — a binding-regime curriculum clamps differentiation as the sole bottleneck, so the evaluator (same-capacity decode of the same target from the same z_harm) tracks differentiation upward by construction; a monotone-coupling PASS is entailed by the ceiling and does not discriminate the driver, and the only discriminating FAIL (evaluator flat below a rising ceiling) is near-impossible by construction. The binding-regime maturation-curriculum build is therefore **REFUSED** (it manufactures a self-fulfilling co-rise rather than testing a driver). The real unblock is a distinct, non-flat, experienced harm-evaluation signal (evaluator ≠ decoder), itself blocked on the committed-action/conversion (F-dominance) ceiling. Combined with the already-noted thinner + counter-indicated lit warrant (Verriotis-Fitzgerald 2016, non-activity-dependent nociceptive maturation), INV-090 **HOLDS** candidate/substrate_conditional with no substrate_queue entry created; governance may retire the driver reading if the commitment ceiling proves durable.
