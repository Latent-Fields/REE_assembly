# MECH-441 disagreement ensemble: `train_step` has no caller -- diagnostic, not a live defect

**Verdict: confirmed vacuous-if-enabled, but NOT currently corrupting any evidence.** MECH-441's
`use_model_disagreement_curiosity` is default `False` on every path, and its falsifier run is
already explicitly HELD (`blocked_substrate`) pending ARC-110 per the 2026-06-27 build decision.
No code change is made here. This documents the gap as a precondition for whenever that hold
lifts, per the task instruction that a training loop is not automatically in scope.

Session: chip `chip-20260823-mech441-ensemble-never-trained`, noticed in passing while building
the SD-063 online head-training loop (`ree-v3` `88287f11c6`, 2026-08-23).

---

## 1. The finding, verified

`ModelDisagreementEnsemble.train_step` (`ree-v3/ree_core/policy/model_disagreement.py:177`) has
no caller anywhere in the tree:

```
grep -rn "\.train_step(" ree-v3 --include=*.py
```

returns exactly four call sites, none of which is the disagreement ensemble:
- `experiments/v3_exq_160_q023_multiagent_convergence_pair.py` -- an unrelated multiagent driver
  (`agent_a.train_step` / `agent_b.train_step`, a different class).
- `tests/contracts/test_sd063_online_head_training.py` -- the SD-063 `E2WorldUncertaintyHead`
  (a different module, `predictors/e2_world_uncertainty.py`).
- `ree_core/agent.py:4245` -- `bla_attribution_head.train_step(...)` (MECH-074d, a third,
  unrelated head).
- `ree_core/predictors/e2_world_uncertainty.py:486` -- that module's own internal
  `self.train_step(...)` recursion.

`agent.py`'s own comment at line 626 names the gap directly: *"The phased-training driver trains
the heads via `disagreement_ensemble.train_step()`; the waking read is no_grad."* No such driver
exists. The only place `disagreement_ensemble` is touched at the agent level besides construction
(`agent.py:644`) is the no-op-guarded, no_grad read at `agent.py:8715-8726` that feeds
`model_disagreement_per_candidate` into E3 selection.

The module's own docstring (`model_disagreement.py:1-49`) already half-documents this as a known,
deliberate hold -- it says the falsifier is `FALSIFIER HELD (blocked_substrate) gated on ARC-110
validation V3-EXQ-707`, but frames the hold entirely around the *single-arena ceiling* finding
(`failure_autopsy_704b-706b-conversion-ceiling_2026-06-27`). It does not mention that the
training driver itself was never built -- i.e. even once ARC-110 clears, the falsifier as
currently wired would still run against an untrained ensemble.

## 2. Is MECH-441 live anywhere today? No.

- `claims.yaml` MECH-441 (`docs/claims/claims.yaml:71176`): `status: candidate`,
  `v3_pending: true`, `epistemic_category: substrate_ceiling`,
  `live_status.reading: candidate/v3_pending/substrate_ceiling`. `implementation_note` states
  the falsifier is HELD pending ARC-110 V3-EXQ-707 and the claim "PROMOTES NOTHING".
- `E3Config.use_model_disagreement_curiosity` defaults `False`; `LatentStackConfig.n_disagreement_heads`
  defaults `0` (ensemble not built at all below `n_heads=2`) -- bit-identical OFF per the module's
  own version-layering doctrine.
- `grep -c use_model_disagreement_curiosity ree-v3/experiment_queue.json` -> `0`. No queued
  experiment references the flag.
- The only driver files that reference the flag at all are the **MECH-440** falsifiers
  (`v3_exq_708[/a/b]_mech440_noisy_selection_head_propagation_falsifier.py`), which set it
  explicitly `False` with the comment `# MECH-441 OFF (this falsifier is the MECH-440 leg only).`
- The only evidence manifest hit (`v3_exq_876a_...json`) is an unrelated MECH-025 run's full
  config dump, also `false`.
- ARC-110 itself (`claims.yaml:74299`) is still `candidate/substrate_conditional` -- unvalidated,
  so the MECH-441 falsifier gate has not lifted.

**No scored DV has ever depended on MECH-441.** This is a dormant substrate, not an active
evidence-validity problem. Nothing to revise in governance.

## 3. Would it be vacuous if switched on? Yes -- measured, using the SD-063 methodology

Reused the relative-spread methodology from
`sd063_online_head_training_keystone_2026-08-22.md` section 4 (which found an untrained
`E2WorldUncertaintyHead` passes the naive `range > 0` gate while being near-uniform, i.e.
vacuous, with `rel_spread` 0.14-0.26 and max/min 1.15-1.28x untrained vs 1.81-2.37 / 10-12x
trained). Applied the same measurement to `ModelDisagreementEnsemble` at random init
(`n_heads=4`, `world_dim=32`, `action_dim=4`, evaluated over 5 distinct action classes at one
fixed `z_world`, 3 seeds):

| seed | rel_spread | max/min | abs range | mean |
|------|-----------:|--------:|----------:|-----:|
| 71   | 0.097 | 1.101x | 3.73e-03 | 3.85e-02 |
| 101  | 0.136 | 1.147x | 5.16e-03 | 3.80e-02 |
| 202  | 0.114 | 1.124x | 2.53e-03 | 2.22e-02 |

This lands squarely inside the SD-063 **untrained/vacuous** band (1.15-1.28x) -- not the trained
band (10-12x). The absolute range is nonzero in every case (it would pass a naive `> 0` readiness
gate, exactly as SD-063 section 4 warns), but it does not discriminate: it is prior-scale noise
from the heads' distinct random inits, not an epistemic signal.

Two further checks isolate the mechanism precisely:

- **The read is completely static.** Two consecutive `disagreement_per_candidate()` calls on the
  identical `(z0, actions)` return bit-identical output (`torch.allclose` True). Since
  `train_step` is never invoked on the live path, the heads' weights never change for the whole
  lifetime of an agent -- there is no experience-dependent variation at all, which directly
  contradicts the module's own headline design claim: *"SELF-ANNEALING is INTRINSIC ... as the
  ensemble trains on visited transitions the cross-head variance collapses toward zero."* That
  property cannot manifest without a caller.
- **The mechanism itself is not broken -- it is only unwired.** Feeding the same ensemble 300
  synthetic P1 `train_step` calls on transitions near `z0` (standing in for the never-built
  phased-training driver) collapsed mean disagreement from `3.56e-02` to `1.15e-05` (~3000x).
  This is the expected Plan2Explore self-annealing behaviour, confirming the defect is a missing
  call site, not a design or implementation bug in `ModelDisagreementEnsemble` itself.

## 4. Conclusion and disposition

This is the same defect class SD-063 fixed for `E2WorldUncertaintyHead` (MECH-314b): a head/
ensemble built with a docstring promise of a "phased-training driver" that was never built,
so any read of it is a random-init artifact rather than a learned signal. The difference here is
severity of consequence, not severity of the code gap: MECH-441's channel is currently
**default-off everywhere and its falsifier is already governance-HELD** pending ARC-110, so
nothing scored is affected and there is no evidence to revise.

**Decision: document, do not build.** Per the task scope, a training loop is not automatically
warranted, and building one now would be premature -- ARC-110 has not validated, so even a
correctly-trained MECH-441 ensemble cannot yet produce a non-vacuous falsifier run (the binding
constraint per `failure_autopsy_704b-706b-conversion-ceiling_2026-06-27` is the single-arena
ceiling, not the curiosity channel). Building the SD-063-style online-training loop
(`train_online` flag, `observe_transition`, bounded replay, warmup) for
`ModelDisagreementEnsemble` is real, scoped, buildable work -- **`complicated (buildable)`**, not
gated on any unresolved unknown -- but it should wait until ARC-110 clears and the MECH-441
falsifier is actually about to run, exactly mirroring how SD-063 was built only once MECH-314b's
per-candidate slot was about to be exercised.

**Action taken:** this diagnostic is the artifact. The module docstring's `FALSIFIER HELD` note
already gates the falsifier on ARC-110; this adds the missing second precondition in one place so
a future `/queue-experiment` session working V3-EXQ-707 (or its successor) does not repeat the
MECH-314b mistake of running the falsifier against an untrained ensemble. No `claims.yaml`
disposition change -- MECH-441 already correctly reads `candidate/v3_pending/substrate_ceiling`
and this finding does not move that.

**Follow-on (chip-worthy when ARC-110 clears, not now):** when ARC-110 validates and V3-EXQ-707
(or successor) is queued to actually run the MECH-441 falsifier, the queueing session must first
build a SD-063-shaped online training loop for `ModelDisagreementEnsemble` (mirrors
`e2_world_uncertainty.py`'s `train_online`/`observe_transition`/replay/warmup additions) and
re-run this diagnostic's relative-spread check post-training to confirm the ensemble has left the
vacuous band before scoring the falsifier. Not spawned as a chip now because it is contingent on
an unresolved upstream gate (ARC-110) and would rot exactly like the withdrawn chips this
practice exists to avoid.
