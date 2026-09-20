# INV-063 leg B: proposed C1 wording, staged for /governance

**Status: STAGED PROPOSAL. Nothing here has been written to `claims.yaml`, `governance_flags.v1.json`
dispositions, `substrate_queue.json` or `experiment_proposals.v1.json`. No experiment was queued.**

- Session `inv063-legb-wording-20260920` (Mac `DLAPTOP`, main checkout), 2026-09-20, at user request.
- Purpose: give /governance a single artifact from which it can apply **GFLAG-0364 / 0367 / 0382
  together**, which is what `failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20` asks for
  ("weigh together -- 0382 carries the contrary number against 0364's re-point").
- This proposes **option (4) / de-pin the readout**, NOT GFLAG-0364's wording as ratified. The
  reason is measurement, and it is section 3.

---

## 1. What is proposed, in two edits

**EDIT 1** replaces the single `Leg B (...)` sentence in INV-063's `what_would_answer` C1.
`Leg B` occurs exactly once in that field, so this is surgical.

**EDIT 2** adds one new outcome clause, `(P-FAIL)`, after `(F3)`. See section 5 for why this is not
scope creep but the missing half of edit 1.

Everything else in `what_would_answer` -- P1-P5, leg A, C2's knee margin, F1-F3, the excluded-legs
block, the second-intake-axis note -- is untouched by this proposal.

## 2. Exact text

### 2a. CURRENT, verbatim from `docs/claims/claims.yaml`

> Leg B (E1 world-model updating): the ACROSS-SLEEP improvement in world-forward
> prediction error, measured on a FROZEN held-out battery with the V3-EXQ-701b/701c frozen-probe
> instrument (pre-sleep PE minus post-sleep PE on the same frozen battery, so the DV is what sleep
> ADDED, not how hard the waking period was), falls monotonically with intake.

### 2b. PROPOSED replacement

> Leg B (E2 world-forward world-model updating -- the `agent.e2.world_forward` head, NOT the E2
> motor-sequence leg excluded below; the "E1" label this sentence carried until 2026-09-20 was prose
> inherited from the description's four-function taxonomy and named a head that does not exist, see
> GFLAG-0355): the ACROSS-SLEEP improvement in a world-forward readout, measured on a FROZEN held-out
> battery (pre-sleep minus post-sleep on the same frozen battery, so the DV is what sleep ADDED, not
> how hard the waking period was) on a CONVERGED base (assert `conv_rel_drop >= 0.99` from measured
> output, never from config), falls monotonically with intake.
>
> THE READOUT IS DELIBERATELY NOT PINNED TO A NAMED OBJECTIVE, because no objective yet measured
> satisfies this leg's own two requirements. Any readout used here must be (i) READABLE on a
> converged base -- the statistic must not sit at its chance or degenerate value, asserted from
> measured output -- and (ii) MOVE IN THE ASSERTED DIRECTION, i.e. the across-sleep delta positive at
> the same setting that satisfies (i). Both candidates measured to date fail one of these. The
> V3-EXQ-701b/701c per-element MSE reconstruction readout is RETIRED from this leg: V3-EXQ-1063
> measured it moving NEGATIVE on a converged base on 3/3 seeds (per-seed -7.14e-05, -6.72e-04,
> -9.22e-04), i.e. a sleep cycle degrades it, so it cannot be read as an improvement that falls with
> intake. The SD-056 InfoNCE frozen-battery objective fails (i) and (ii) SIMULTANEOUSLY in its readout
> temperature: on V3-EXQ-798a's configuration, readability (headroom > 5% of ln K) requires
> `tau <= 0.01` while a positive across-sleep delta requires `tau >= 0.03`, with no overlap
> (GFLAG-0382; n=1 seed, 1800-step P0, one sleep cycle). SUPPLYING A READOUT THAT MEETS (i) AND (ii)
> TOGETHER IS THE SUBSTRATE DEPENDENCY THIS LEG IS BLOCKED ON, and any re-queue must demonstrate it
> BEFORE the four-arm ladder is worth running.

### 2c. PROPOSED new outcome clause, after (F3)

> (P-FAIL) PRECONDITION NOT MET. F1, F2 and F3 are each conditioned on "P1-P5 all met", so a run --
> or a diagnostic short of a run -- that establishes a precondition CANNOT currently be met has no
> registered outcome here and must NOT be read as any of the three. Pre-registered consequence: the
> claim converts to `epistemic_category: substrate_conditional`, `status` stays `candidate`, the
> failing precondition is named with the measurement that failed it, and no further experiment budget
> is spent on this falsifier until the named substrate exists. This is a legitimate and useful
> outcome and is NOT a falsification -- F1 is the falsification, and F1 requires P1-P5 to have been
> met. First exercised 2026-09-20 (GFLAG-0389 / GFLAG-0390).

## 3. Why not GFLAG-0364 as ratified

GFLAG-0364's wording pins the readout to SD-056 InfoNCE, and GFLAG-0367 establishes that it must
then also pin the temperature (at the shipped `tau = 0.1` the readout sits at 99.5% of chance and
cannot carry C1/C2 at all). The user-ratified pin was `tau = 1e-3`.

GFLAG-0382 then measured that pin **in the ladder's own regime** (798a configuration, converged base
`conv_rel_drop` 0.9899, K=64, seed 42):

| tau | headroom (% of ln K) | readable (>5%)? | across-sleep delta | direction as asserted? |
|---|---|---|---|---|
| 0.1 (shipped) | 0.62% | no | +1.55e-03 | yes |
| 0.03 | 2.02% | no | +3.56e-03 | yes |
| 0.01 | 5.65% | yes | -7.18e-04 | no |
| 0.003 | 14.61% | yes | -7.68e-02 | no |
| **0.001 (the ratified pin)** | **18.54%** | **yes** | **-3.89e-01** | **no** |

At the ratified pin the readout has ample headroom and **sleep makes it worse** -- the identical
condition that retired the 701b MSE readout and was the entire reason for the re-point. Pinning it
would register an assertion ("the across-sleep IMPROVEMENT") against the only in-regime measurement
of it.

The trade-off looks structural rather than a tuning accident: as `tau -> 0` the softmax sharpens
toward a hard nearest-neighbour test that a sleep pass degrades on an MSE-converged head (GFLAG-0360's
E1-vs-E2 argument); as `tau -> infinity` the loss flattens toward `ln(K)` where every delta is tiny,
positive and uninformative.

**Limits, stated rather than papered over** (unchanged from GFLAG-0382): n=1 seed -- seed 123's P0 was
cut by a shell timeout; P0 was 1800 steps, not the 5400 the ladder would use; one sleep cycle. This is
enough to decline to REGISTER the pin. It is NOT enough to assert leg B is permanently unreadable,
which is why 2b states a requirement rather than a verdict, and why (P-FAIL) converts rather than
falsifies.

## 4. Two corrections this wording carries, both found by reading the field

**4a. GFLAG-0355's bare E1 -> E2 relabel would COLLIDE if applied literally.** GFLAG-0355 is correct
that `E1DeepPredictor` has no `world_forward` head and that the DV named in the sentence is an E2
measurement. But INV-063's excluded-legs block already carries a DIFFERENT E2 leg -- "E2
motor-sequence learning", excluded on the MECH-457 competence floor. A sentence reading simply "Leg B
(E2 world-model updating)" sits two paragraphs above an exclusion of "E2 ...", and a later reader has
to re-derive which E2 is meant. 2b therefore names the head (`agent.e2.world_forward`) and says
explicitly which leg it is not. GFLAG-0364's proposed wording ("Leg B (E2 world-model updating; see
GFLAG-0355 ...)") has this ambiguity; this is the one substantive way 2b differs from it beyond the
readout question.

**4b. The claim's outcome space had no precondition-failure route, and today's conversion had no
registered basis in the claim's own text.** The phrase circulating in GFLAG-0382 and in the
`evidence_quality_note` -- that the claim's own text calls conversion "a legitimate, useful outcome"
-- is not in `what_would_answer`. Searched: no occurrence of "legitimate", "escape", or any
precondition-failure branch; F1-F3 are each explicitly gated on "P1-P5 all met". The GFLAG-0390
conversion was the right call and is now applied, but it was applied through a route the falsifier
does not register. Edit 2 registers it. Without it, a future reader can reasonably read a P-gate
failure as F1 (flat -> "genuinely falsified"), which would be wrong by the claim's own logic.

## 5. What this does NOT change, so no one reads more into it

- **Does not reverse the `substrate_conditional` conversion** (GFLAG-0390, user decision
  2026-09-20). It makes the falsifier text consistent with it.
- **Does not queue V3-EXQ-1071.** The driver stays at ree-v3 `9700362aa5`, unqueued and reusable, per
  the `evidence_quality_note`. There is no experiment budget on this claim.
- **Does not unblock the four-arm ladder even if a readout appears.** Leg A is independently blocked:
  all three registered C1 leg-A DVs are transforms of the same MEL scalar that P1's manipulation check
  gates on (GFLAG-0389, `inv063_legA_dv_circularity_20260920.md`), so leg A must be RE-REGISTERED with
  a DV independent of `e3_prediction_error` first. That re-registration is owed and is NOT drafted
  here.
- **Does not touch** `status` (stays `candidate`), confidence, the five 2026-09-08 literature entries,
  C2's knee margin (which self-computes from a four-arm run's own data and needs no amendment, per
  GFLAG-0367 (2)), or the `non_contributory` dispositions of V3-EXQ-1063 and 1069.

## 6. Proposed flag dispositions, for /governance to accept or revise

| Flag | Type | Proposed disposition |
|---|---|---|
| GFLAG-0364 | contested_disposition | **APPLY WITH REVISION** -- the MSE retirement is applied verbatim (uncontested: 9/9 cells negative on a converged base); the InfoNCE pin is NOT applied, superseded by GFLAG-0382's in-regime measurement. Resolution note should record that the 2026-09-19 user ratification was of the re-point, on evidence that GFLAG-0382 later contradicted in the ladder's own regime. |
| GFLAG-0367 | evidence_discrepancy | **RESOLVE as incorporated** -- (1) the temperature mechanism and (2) the units correction are both carried into 2b/section 3; its point (3) on P1 is superseded by V3-EXQ-1069, which passed 2/3. Its "which task leg B means" observation (state-identity vs action discrimination) remains live and should ride into the substrate dependency named in 2b. |
| GFLAG-0382 | evidence_discrepancy | **RESOLVE as applied** -- it is the measurement this wording is built on; its n=1 limit is carried into the text as a requirement rather than a verdict. |
| GFLAG-0355 | stale_note | **PARTIALLY DISCHARGED** by edit 1 for this sentence, with the collision in 4a fixed. Its SECOND, separate item -- `substrate_queue.json` entry `e2-world-forward-sleep-trainer` still reading `pending_implementation` although the build landed 2026-09-17 as ree-v3 `4610133` -- is NOT addressed here and the flag should stay open for it. |

Cross-refs: GFLAG-0359, GFLAG-0360, GFLAG-0389, GFLAG-0390;
`evidence/planning/inv063_legb_tau_bind_20260920.md`;
`evidence/planning/inv063_p1_gate_and_infonce_tau_20260919.md`;
`evidence/planning/inv063_legA_dv_circularity_20260920.md`;
`evidence/planning/failure_autopsy_INV-063-1060-1063-1069-cluster_2026-09-20.md`.
