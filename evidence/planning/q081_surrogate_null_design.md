# Q-081 — Constrained-Realisation Surrogate Null: Design Record

**Status:** BUILT + VALIDATED (2026-07-22)
**Gates:** `Q-081` (non-degeneracy guard), `MECH-466`, `INV-091`, `ARC-112`
**Code:** `ree-v3/experiments/_lib/q081_surrogate.py`
**Validation:** `ree-v3/tests/contracts/test_q081_surrogate_null.py` (22 tests, all passing)
**Upstream:** telemetry audit `q081_cross_stream_telemetry_audit.md`; recorder
`ree-v3/experiments/_lib/stream_recorder.py`; guard sharpened in REE_assembly `ca8e3d7fc8`

---

## 1. Why this needed designing rather than looking up

Q-081's guard names the construction — a block permutation within each stream's own tick
grid — and names its reference, Lancaster et al. 2018 (*Physics Reports* 748:1–60). The
claim text also flags the gap, and it is the whole of the design problem:

> the reference treats a common regular grid, while REE's streams tick at 1, 3 and 10
> steps, so this surrogate must be DESIGNED for REE rather than looked up — the step
> where an error is easiest to make and hardest to notice.

The surrogate literature is written for signals sampled together. REE's are not: E1 ticks
every step, E2 every 3, E3 every 10 (SD-006). Everything below follows from that one fact.

## 2. What the surrogate replaces, and why the replacement was necessary

`stream_recorder.rate_matched_shuffle_index()` — the control that existed before this work
— permutes each stream's **fresh samples individually** and leaves held samples in place.
It preserves tick times and the marginal but **not within-stream autocorrelation**. That is
the exact failure Lancaster's constrained-realisation principle exists to prevent:
significance achieved by destroying something that was never under test, i.e. a **false
Outcome A**.

This is not a theoretical worry, and the contract does not merely assert it — it
**exhibits** it. On two streams built from *provably independent* noise (`coupling=0.0`)
but each strongly autocorrelated:

| null construction | uncoupled seeds significant at p<=0.05 |
|---|---|
| fresh-only shuffle (superseded) | **6 / 8** — false Outcome A |
| block permutation (this module) | **0 / 8** — correct |

`test_naive_shuffle_produces_the_false_positive` pins both numbers. **Do not use the
fresh-only shuffle to adjudicate Q-081.**

## 3. The unequal-rate rule

### The natural mistake

Pick one block length `L` in ticks and apply it to every stream. At `L = 20`, E1 blocks span
20 steps and E3 blocks span 200. The streams are then scrambled at different temporal
granularities: each coarse block spans ten fine blocks, so the coarse stream's large-scale
layout survives largely intact relative to the fine stream's, and cross-stream alignment is
destroyed **unevenly across the pair**. The ensemble is no longer a null for the same
hypothesis on every pair — and nothing downstream reports this.

### The rule adopted

Choose **one common block duration `W` in STEPS** — the only unit the streams share — and
derive each stream's block length in its own tick units:

```
L_s = max(1, round(W / period_s))
```

Blocks are then temporally commensurate, and alignment is destroyed at the same timescale
for every pair. A useful consequence falls out: the block **count** equalises across
streams,

```
n_blocks_s  ~  m_s / L_s  ~  (n_steps/period_s) / (W/period_s)  =  n_steps / W
```

so the ensemble is equally rich for the fine and the coarse stream. That equalisation is
the reason `W` is measured in steps and not ticks.
`test_block_lengths_are_commensurate_across_e1_e2_e3_rates` pins this over 1/3/10.

### Choosing W — two constraints from opposite directions

- **Lower.** `W >= safety * max_s (tau_s * period_s)`, floored at `max_s period_s` so the
  coarsest stream gets `L_s >= 1`. Blocks shorter than the correlation time cannot carry
  it, and property (c) fails for the slowest-decorrelating stream. `safety = 2` by default,
  standard block-bootstrap practice.
- **Upper.** `W <= n_steps / min_blocks` (default 8), or the permutation ensemble is too
  coarse to have variance.

**If those cross, `plan_blocks()` RAISES** with the `n_steps` that would be needed. It does
not shrink the blocks to fit. This is the single most important defensive decision in the
module: a surrogate that quietly violates (c) produces a plausible p-value with no
symptom, which is precisely the "easiest to make, hardest to notice" error. Refusal is the
only safe failure mode. Pinned by `test_plan_refuses_a_run_too_short_for_its_own_autocorrelation`.

### Periods and taus are measured, never assumed

`agent.clock` resets the E3 phase under MECH-091 and modulates the rate under MECH-093, so
a nominal `step % 10` is wrong on real traces. Periods come from the recorded
`<name>__fresh` flags (median inter-fresh gap); `tau` is a 1/e first-crossing of the ACF
computed **on the fresh subsequence only**. Excluding held samples matters: they are
repeats, and including them would inflate `tau` by the hold length — i.e. by the update
rate — smuggling rate dependence back into the analysis.

### Hold semantics are classified, not guessed

Permuting fresh samples means the held steps have to be rebuilt, and rebuilding them wrongly
changes the marginal. The recorder writes two genuinely different hold semantics, so
`classify_hold_mode()` measures which applies per stream:

- `carry` — a held row repeats the previous row (`e3_commitment`, `e3_scores`,
  `operating_mode`). Rebuilt by forward-filling the **new** value.
- `filler` — every held row is the same constant, unrelated to the last fresh value (the
  event streams record `[0, nan]` on a non-event step). Left alone; carrying it would
  invent events that never fired.
- `none` — fresh every step (`z_world`, `z_self`).
- `unstructured` — neither, so `block_permute_stream()` **refuses**.

A random **circular offset** is applied before cutting blocks, so boundaries fall
differently in each ensemble member; without it every surrogate cuts at the same points and
the ensemble understates the null's variability.

## 4. Requirement 2 — validating the null before it adjudicates anything

Shipped as a contract, not a notebook, so that "before it adjudicates anything" keeps being
true as the substrate moves.

| Requirement | Test | Result |
|---|---|---|
| **KILL** a deliberately-artefactual statistic (computed purely from update periods) | `test_null_kills_the_artefactual_statistic` | p = 1.0; **bit-identical** on every member; 1 distinct value |
| **SPARE** a deliberately-injected real relation | `test_null_spares_an_injected_real_relation` | p <= 0.05 on **4/4** seeds |
| Reject the autocorrelation-only false positive | `test_block_surrogate_rejects_the_autocorrelation_false_positive` | non-significant on **4/4** seeds |
| Exhibit the superseded shuffle's failure | `test_naive_shuffle_produces_the_false_positive` | naive 6/8 vs block 0/8 |
| (a) tick times preserved | `test_surrogate_preserves_tick_times_exactly` | exact |
| (b) marginal preserved | `test_surrogate_preserves_the_marginal_exactly` | exact on the fresh subsequence |
| (c) within-stream autocorrelation preserved | `test_surrogate_preserves_within_stream_autocorrelation` | block >= 0.5x data; shuffle <= 0.25x |

The KILL test asserts **exact invariance**, not just a large p-value. The surrogate
preserves freshness flags exactly, so any function of them alone is bit-identical across the
ensemble; the p-value is the consequence, the invariance is the mechanism, and the mechanism
is what a future edit could break.

Ground truth is why the fixtures are synthetic rather than agent-driven: validating a null
is a statement about the *construction*, and it requires knowing whether a real relation
exists — which no agent trace can supply. Rates 1/3/10 mirror SD-006.

Note on (b): the **fresh-subsequence** marginal is exact. The full-series marginal is exact
only when hold run-lengths are constant; under a MECH-091 phase reset they are not, so the
honest statement of what is preserved is the fresh-sample marginal.

## 5. The a-priori filter, made mechanical

Q-081 rules out, before any run, any candidate statistic that is a function of the
configured update rates. `screen_statistic()` implements that filter **mechanically rather
than by inspection**, using the property that makes such a statistic useless:

> A statistic constant across the whole surrogate ensemble is a function only of what the
> surrogate *preserves* — tick times, marginal, within-stream autocorrelation — and so
> cannot carry information about the between-stream relation, which is the only thing the
> ensemble varies. Its p-value is meaningless however extreme its value looks.

Verdict is `ruled_out` or `admissible`. Run it on every candidate statistic before that
statistic adjudicates anything. `admissible` is a necessary condition, not an endorsement of
the statistic's scientific meaning.

## 6. Lag is a control quantity

Recorded in the claim as an Outcome-B (clock) detector: a lag between streams ticking at
1/3/10 steps is **guaranteed by the scheduler** with no shared organisation whatever
(Chang, Nastase & Hasson 2022 is the worked analogue, in a milder form — fMRI's confound is
haemodynamic filtering; REE's is the scheduler itself, which is worse).

`cross_stream_xcorr()` returns the lag alongside the statistic, and `lag_control_report()`
labels it `role="control"` with the interpretation string spelled out, plus
`scheduler_expected_lag_steps` — the amount attributable to the rate offset alone — so a
reader can see at once whether the measured lag is anything more. The reporting contract:
**it must be present and must not explain the result.** Pinned by
`test_lag_is_reported_as_a_control_not_a_readout`. Do not promote it to the primary readout.

## 7. Ceiling — what this does NOT deliver

Restated because it is load-bearing and easy to lose once a p-value exists:

**Clearing this null is NECESSARY for Outcome A and nowhere near sufficient.** Wired
coordination is real coordination and will correctly clear any surrogate test. The surrogate
destroys cross-stream alignment *in the analysis*; only the **structure-destroying arm** (BUILT 2026-07-22 — `q081_landmark_removal_arm_design.md`) —
removing event/commitment landmark structure while leaving streams, rates and environmental
input statistics intact — destroys it *in the system*, and only the ablation series
separates Outcome A from Outcome B. A statistic that survives that arm was measuring the
clock.

This module builds the null. It does not adjudicate the claim.

## 8. What remains before Q-081 can be run

| Piece | State | Owner |
|---|---|---|
| Retrospective telemetry audit | DONE (`4fb39223a9`) — verdict: not testable retrospectively | closed |
| Per-step multi-stream recorder | IN FLIGHT | session `suspicious-williamson-73da0d` |
| **Constrained-realisation surrogate + null validation** | **DONE — this record** | this session |
| Prospective recording run (experiment script + queue entry) | NOT STARTED — must go through `/queue-experiment` | unowned |
| Structure-destroying (landmark-removal) arm | **DONE (2026-07-22)** — `experiments/_lib/q081_landmark_removal.py`; experiment-layer, no ree_core change. Record: `q081_landmark_removal_arm_design.md` | closed |
| Ablation series (the only A-vs-B discriminator) | NOT STARTED | unowned |

The surrogate is usable independently of all of the above: it consumes the recorder's array
format (`name`, `name__fresh`) and nothing else.
