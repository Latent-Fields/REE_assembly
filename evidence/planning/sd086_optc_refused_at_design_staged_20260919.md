# SD-086 option C -- REFUSED AT DESIGN by the red-team pass, with confirming measurements

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or any other registry). NO EXPERIMENT WAS QUEUED; `experiment_queue.json` is untouched.**

- Session: `metaworker-science-20260919-sd086-optc-exq-1064` (headless)
- Chip: `chip-proposal-exp-1222-paced` | Claim: **SD-086** | Proposal: **EXP-1194** (`EVB-1666`)
- Reserved and then released: **V3-EXQ-1064**
- Recorded: 2026-09-19T07:20:00Z
- Red-team model: **fable** (session model: Opus 5). Verdict: **BLOCKING**.
- Driver kept in-tree, bannered REFUSED, NOT queued: ree-v3 `59f7bd87e3`,
  `experiments/v3_exq_1064_sd086_zharma_vector_vs_norm_decode.py`

---

## 1. The design, as the user pinned it

User decision 2026-09-19T07:06:24Z (OPTION M): queue SD-086 option C with the JOINT target.
Decode `[hazard_at_agent, resource_at_agent]`; PASS iff the mean vector-minus-norm held-out R^2
margin exceeds BOTH 2x its cross-seed SD AND 0.10 absolute, over >= 3 seeds, with
`p0h_readiness_met` TRUE asserted as a precondition.

The driver was written, smoke-tested (PASS), and passed
`validate_experiments.py --strict` with zero warnings after three advisory fixes.

## 2. The refusal

**The design PASSES on an UNTRAINED encoder.** Measured by this session at the real eval budget
(600 ticks), 3 seeds, identical in every respect except whether the P0h stage ran:

| | vector R^2 | norm R^2 | margin | mean | 2xSD band | C1 | C2 | PASS |
|---|---|---|---|---|---|---|---|---|
| **UNTRAINED** (frozen random projection) | 0.9827 .. 0.9995 | +0.345 .. +0.469 | +0.513 .. +0.654 | **+0.5768** | 0.1169 | T | T | **PASS** |
| **TRAINED** (P0h ON) | 0.9993 .. 1.0000 | +0.321 .. +0.634 | +0.365 .. +0.679 | **+0.5515** | 0.2698 | T | T | **PASS** |

The manipulation under test -- training the encoder -- moves the scored statistic by 0.025, well
inside the noise band, and does not change the verdict.

### Root cause

**The scored decode targets ARE two coordinates of the encoder's own INPUT.**
`ree_core/environment/causal_grid_world.py` ~3037-3038 writes `hazard_at_agent` into
`harm_obs_a[:25]` and `resource_at_agent` into `harm_obs_a[25:]`; the driver reads those same
halves back as its targets. `AffectiveHarmEncoder` is a 58 -> 64 -> 16 MLP operating over a very
small input range, i.e. near-linear, so its 16-d output linearly reconstructs its own input **for
any weights, trained or not**. Hence `vector_r2` is pinned at ~1.0 and

    margin  ==  vector_r2 - norm_r2  ~=  1 - norm_r2

so both pre-registered criteria are decided **entirely by `norm_r2`**. What the design measures is
"16 dims beat 1 dim at reconstructing a rank-2 input" -- a statement about RANK, true of a random
projection, and not a statement about what training put into `z_harm_a` nor about the readout FORM
that SD-086 is a claim about.

### Second defect, same root -- and it was mine

The headroom precondition I added at the validator's prompting, `min(1 - norm_r2) > 0.10`, was
meant to stop C2's absolute floor being unreachable. Once `vector_r2` is pinned at ~1, that
precondition **implies** C2 (`mean margin > 0.10`): worst-seed headroom > 0.10 forces the mean
margin above 0.10. So **C2 cannot fail on any run that is scored at all** -- the gate intended to
keep C2 honest instead made it unfalsifiable.

## 3. This also invalidates the scoping probe the OPTION M decision rested on

The 2026-09-19T04:55Z scoping measurement
(`sd086_optc_decode_target_scoping_staged_20260919.md`) reported that all four candidate targets
cleared, with margins +0.34..+0.80, and recommended the joint target partly because "every
candidate clears". **That measurement is confounded by the same mechanism**: every candidate was
an input coordinate (`hazard_at_agent`, `resource_at_agent`, their pair) or a near-function of one
(`per_tick_harm_exposure`), so all four were trivially reconstructable from the 16-d vector by any
projection. The uniform clearing I reported as "robustness" was the artifact, not the signal.

The one reading from that document that SURVIVES is the frozen-vs-trained comparison of the
NORM's decodability (0.977 frozen vs 0.647 trained on hazard) -- that concerns the norm, which is
not pinned. Everything I inferred there from the VECTOR's R^2 should be discarded.

## 4. What a sound successor needs (NOT designed here -- that is the user's call)

Stated so the refusal is actionable, not as a proposal this session is authorised to pick:

- The decode target must be something the encoder's input does **not** already contain verbatim --
  otherwise the vector arm is reconstruction, not readout. Candidates a human should rule on: a
  target at a temporal offset (predicting a FUTURE harm quantity), a downstream consumer's
  quantity (E3 commit behaviour), or a held-out env property not written into `harm_obs_a`.
- The comparison should include at least one **trained scalar head** arm, since SD-086's actual
  claim is "calibrated scalar head beats norm", and a 16-d-vector-beats-norm result cannot
  distinguish "the norm is the wrong readout" from "any 1-d readout is".
- The headroom gate must not be computable from the same quantity the load-bearing criterion
  routes on, or it re-creates the implication above.
- The 50/50 time split runs over an `harm_obs_a_ema` that persists across `env.reset()`
  (`causal_grid_world.py:1977`), so the two halves are different regimes and held-out R^2 is
  unbounded below. A 1-parameter fit extrapolates badly under that shift, which is part of why the
  norm arm scores as poorly as it does. A successor should split by episode with the EMA reset, or
  state explicitly that regime-shift extrapolation is part of what it measures.

## 5. Process record

- Red-team pass ran ONCE, in the foreground, on a different model (fable), per the skill. It was
  not iterated to CLEAR.
- Every finding it raised was verified against the source before being acted on. The BLOCKING
  finding was confirmed by an independent measurement written by this session (table in section 2),
  not accepted on the reviewer's say-so.
- Per the campaign's consent rule -- "if the red-team refuses the design, that is a result: record
  it and report it; do not re-design around the refusal on your own" -- **no alternative design was
  substituted.** Section 4 names constraints, not a chosen design.
- V3-EXQ-1064 was reserved via `task_claim.py` and is released unused; the id is burned for
  clarity of the record rather than recycled.

## 6. Reproduction

```
cd /Users/dgolden/REE_Working/ree-v3
# the refused driver (bannered, not queued):
#   experiments/v3_exq_1064_sd086_zharma_vector_vs_norm_decode.py   (ree-v3 59f7bd87e3)
# section 2's table: build an agent with _make_agent, optionally run run_zharm_a_p0,
# then _collect + _margin on the joint target -- with and without the P0h call.
```
