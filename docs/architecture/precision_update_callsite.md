# Precision update call site (Q-042)

Architectural decision doc supporting `Q-042` in `docs/claims/claims.yaml`.

## The problem

`E3Selector._running_variance` is the precision signal feeding the BG commit gate
(`commit when running_variance < threshold`) and several downstream modules
(dACC precision-weighted PE per MECH-258, descending modulation gates, AIC
urgency scaling). Its update path is:

```
agent.update_residue()
    -> e3.post_action_update(actual_z_world, harm_occurred)
        -> e3.update_running_variance(prediction_error)
            -> _running_variance EMA write
```

Experiment scripts must remember to call `agent.update_residue()` after each
step. When they forget, the entire chain is dormant: `_running_variance` stays
at `precision_init=0.5` for the whole run, the BG commit gate never fires, and
`current_precision = 1/(0.5 + 1e-6) = 1.999996` constant.

This is the root cause of the 2026-05-07 EXQ-514d/514e/524/530/536 cluster
(see `evidence/experiments/review_tracker.json` discussion note
`2026-05-07T23:12Z_rv_pinned_cluster`). The same omission pattern produced the
parallel `update_z_goal` cohort fix the same week (11 scripts, 4 currently-
weighting manifests superseded).

## Two options considered

### Option A — contract enforcement (current direction)

Keep `update_running_variance()` inside the post-action / outcome-integration
hook. Make calling it mandatory:

- `ree-v3/experiments/_harness.py StepHarness` enforces canonical
  `sense / update_z_goal / update_residue` sequence with kwargs-only call shape.
- `tests/contracts/test_step_harness_contract.py` pins the signature and
  end-to-end smoke.

Reading: precision is *defined* as the running variance of observed prediction
errors, so it lives downstream of action AND downstream of outcome arrival.
The call-site location encodes "rv tracks how surprising real outcomes were."

### Option B — early update / hoist into `select_action()`

Move (or duplicate) the rv update into `agent.select_action()` or a dedicated
`post_action()` hook that always fires regardless of downstream loop content.

Reading: precision is a control-plane state that should be live whenever the
agent is selecting actions.

## Evidence

### Biology

Where in the action–outcome loop is the analogous "precision of prediction
error" actually computed in cortex / basal ganglia?

| paper | finding | timing |
|---|---|---|
| Behrens et al. 2007 (Nat Neurosci, [PMID 17676057](https://pubmed.ncbi.nlm.nih.gov/17676057/)) | ACC volatility encoding predicts behavioural learning rate | confined to outcome-monitoring period |
| Nassar et al. 2012 (Nat Neurosci, [PMID 22660479](https://pubmed.ncbi.nlm.nih.gov/22660479/)) | pupil-linked LC change-point probability driven by most-recent-outcome PE | post-outcome; tonic baseline pupil sits across trials |
| Aston-Jones & Cohen 2005 (Annu Rev Neurosci, [PMID 16022602](https://pubmed.ncbi.nlm.nih.gov/16022602/)) | LC phasic bursts driven by outcome of task-related decision processes | post-decision-evaluation; tonic LC slow separate channel |
| Yu & Dayan 2005 (Neuron, [PMID 15944135](https://pubmed.ncbi.nlm.nih.gov/15944135/)) | ACh = expected uncertainty (slow, action-time-stable); NE = unexpected uncertainty (event-driven) | two estimators on different schedules; NE updates on surprising outcomes |
| Friston et al. 2017 active inference | sensory attenuation at action time: precision on sensory PE is transiently suppressed pre-action, dominant precision update follows outcome | outcome-time |

The variance estimator is fundamentally an outcome-driven quantity. Action-time
has its own gain channel (tonic LC, attentional precision) but it is a *read*
of slow precision, not the moment the running variance is rewritten.

### AI / ML workhorses

| system | running statistic | update site |
|---|---|---|
| Kalman / particle filter | covariance | only at update step (post-observation) — textbook predict-then-update |
| PPO / SAC / A2C (Stable-Baselines3, [Huang et al. ICLR Blog Track 2022](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/)) | advantage / reward / value running stats | over the rollout buffer after collection, in the learn phase |
| DreamerV3 ([Hafner et al. Nature 2025](https://www.nature.com/articles/s41586-025-08744-2)) | RSSM posterior, KL precision, percentile return normalisation, critic value stats | world-model training step, after experience added to replay |
| MuZero | value statistics, target normalisation | training step on collected trajectories |
| Active inference (Friston) | precision π | gradient descent on free energy *given observations* — post-outcome |

In every workhorse, the running statistic is rewritten on outcome arrival /
during the learning phase, not inside the action-selection forward pass.

## Verdict

Biology and ML converge on the same answer: **Option A is correct.** Running
variance on prediction error is, by definition, a quantity over observed PE
magnitudes, which only exist after the outcome.

Hoisting it into `select_action()` (Option B) would either:
- update variance on a stale PE from the previous step (off-by-one), or
- require a forward simulation to fabricate a PE, which conflates expected
  with realised variance — exactly the conflation Yu & Dayan and the active-
  inference literature warn against.

The robustness problem (scripts forgetting `update_residue()`) is a software-
contract issue, not an architectural one.

## Recommended actions

1. **Keep Option A.** No change to the rv update call site.
2. **Add a regression test** at `ree-v3/tests/contracts/test_running_variance_contract.py`
   that runs a representative 100-step random-action episode and asserts
   `e3._running_variance` changes by more than `1e-6` from `precision_init`.
   This catches scripts that bypass StepHarness or delete a post-action hook.
3. **If a future use case needs a live precision read at action time without
   outcome integration**, expose a *separate* tonic / baseline precision channel
   (the Aston-Jones tonic-LC analog) rather than collapsing both regimes into
   `_running_variance`. This separation matches the Yu & Dayan ACh / NE
   architecture: expected uncertainty (action-time read) and unexpected
   uncertainty (outcome-time write) are different signals on different
   timescales.

Q-042 promotes from `open` to `candidate-resolved` once the regression test
lands and at least one V3 experiment exercises both StepHarness and the new test.

## Sources

- Behrens et al. 2007 — Learning the value of information. https://pubmed.ncbi.nlm.nih.gov/17676057/
- Yu & Dayan 2005 — Uncertainty, neuromodulation, and attention. https://pubmed.ncbi.nlm.nih.gov/15944135/
- Aston-Jones & Cohen 2005 — LC-NE adaptive gain. https://pubmed.ncbi.nlm.nih.gov/16022602/
- Nassar et al. 2012 — Pupil-linked arousal as evidence integration. https://pubmed.ncbi.nlm.nih.gov/22660479/
- Friston et al. 2017 — Active Inference: A Process Theory. https://activeinference.github.io/papers/process_theory.pdf
- Hafner et al. 2025 — DreamerV3. https://www.nature.com/articles/s41586-025-08744-2
- Kalman filter — https://en.wikipedia.org/wiki/Kalman_filter
- Huang et al. 2022 — 37 Implementation Details of PPO. https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/
- Stable-Baselines3 PPO docs — https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html
