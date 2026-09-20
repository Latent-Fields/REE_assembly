# V3-EXQ-1043b AMBER pre-flight smoke -- the random rank-r reference distribution

Recorded 2026-09-20T14:01:57Z by `metaworker-science-20260920-exq1043b-mech537-random-subspace`
on `ree-cloud-4` (linux-x86_64, torch 2.12.0+cpu, python 3.10.12).
Machine-readable companion: `v3_exq_1043b_randrank_reference_smoke_20260920.json`.

**This is a PROBE, not an experiment.** No manifest, no `claim_ids`, no queue entry. It
measures the INSTRUMENT V3-EXQ-1043b would be built from, and it contributes nothing to
MECH-537's evidence either way.

Authority: the CONFIRMED autopsy `failure_autopsy_V3-EXQ-1043a_2026-09-20.json`
(`routing_detail.successor`), ratified by `/governance` cycle governance-20260920, and the
AMBER pre-flight recorded on `chip-20260920-exq1043b-mech537-random-subspace-reference` by
`orchestrate-20260920-1121`, whose two named items are exactly what this probe settles.

## What it does, and why it needs no warmup

The `ws250_randrank` arm is `_project(x_standardised, b_rand)` -> `x1002._train_adapter` ->
`x1002._agreement`. It reads ONLY the sender `world_state` and the oracle labels. Neither
touches the warmed-up encoder, so the WITHIN-SEED DRAW DISTRIBUTION of `D_randrank` is
measurable exactly, at the real sample size, without the ~1.8 h/seed warmup. `r` is pinned
per seed to the parsimonious rank V3-EXQ-1043a actually recorded (11/11/10/8/10/10).

`D_comm` is NOT recomputable this way (it needs the fitted receiver), so wherever `D_comm`
appears below it is V3-EXQ-1043a's RECORDED value, used as an indicative reference point --
never as a measurement of 1043b's statistic.

**Pipeline fidelity, checked per seed and OK on 6/6**: `n_sender_dims_live` (146),
`heldout_steps` (2148/2061/1965/2001/2162/2050) and `strongest_trivial_agreement` all match
the landed 1043a manifest exactly. Recomputing the C2 CI from 1043a's recorded single draws
reproduces the autopsy's `[0.0051, 0.0948]` to four decimals, so the probe is reading the
same numbers the autopsy did.

## Result 1 -- COST (AMBER item 1): settled, and the premise was right for the wrong reason

| operation, at the real shapes | wall time |
|---|---|
| one decoder fit (`_train_adapter`, 60 passes, ~5000 train rows) | **~1.6 s** |
| one `communication_subspace` refit at a single rank (grouped 5-fold CV) | **~0.06 s** |

The RRR refit is ~25x CHEAPER than the decoder fit, so 1043a's 200-replicate permutation
loop cost ~332 s/seed almost entirely in DECODER fits, not in the refits the autopsy's
"strictly cheaper than 1043a's 200 refits per seed" phrasing points at. Dropping the RRR
refit therefore saves ~4% per replicate; the saving that matters comes from `B < 200`.

| B | SE of the draw-mean comparator | cost/seed | vs the 1043a permutation loop |
|---|---|---|---|
| 20 | 0.0055 | 32 s | 10% |
| 50 | 0.0035 | 80 s | 24% |
| 100 | 0.0024 | 160 s | 48% |
| 200 | 0.0017 | 320 s | 96% |

## Result 2 -- IS MANY-DRAW AVERAGING WORTH IT? Yes, and the variance is real orientation noise

`x1002._train_adapter` **never seeds anything** -- its `seed` and `arm_id` arguments are
print labels only; `_make_adapter` and `torch.randperm` both draw from the ambient global
RNG. So repeated fits of the SAME subspace differ, and the draw spread had to be decomposed
before it could be read. B=24 independent draws against K=8 refits of ONE fixed draw:

| seed | r | sd total | sd decoder-only | sd orientation |
|---|---|---|---|---|
| 42 | 11 | 0.0191 | 0.0050 | 0.0184 |
| 43 | 11 | 0.0216 | 0.0067 | 0.0205 |
| 44 | 10 | 0.0247 | 0.0070 | 0.0237 |
| 45 | 8  | 0.0309 | 0.0037 | 0.0307 |
| 46 | 10 | 0.0239 | 0.0064 | 0.0230 |
| 47 | 10 | 0.0264 | 0.0045 | 0.0260 |
| mean | | **0.0244** | **0.0055** | **0.0237** |

~94% of the draw-to-draw variance is genuine SUBSPACE-ORIENTATION variance; decoder-training
noise is a small, separable term. Single-draw noise (0.0244) is of the same order as the
cross-seed sd of the landed C2 contrast (0.0427) -- i.e. roughly a third of the variance in
1043a's headline statistic was the single draw. Averaging it out is worth doing.

## Result 3 -- THE READINESS GATE (AMBER item 2): the candidate formulas DISAGREE, 0/6 vs 6/6

Margin of the random rank-r arm over the strongest trivial predictor, per seed:

| seed | 1043a's single draw | mean over B=24 draws | max over B=24 draws |
|---|---|---|---|
| 42 | +0.0205 | +0.0364 | +0.0833 |
| 43 | +0.0543 | +0.0402 | +0.0917 |
| 44 | +0.0132 | +0.0122 | +0.0514 |
| 45 | +0.0085 | **-0.0219** | +0.0525 |
| 46 | +0.0157 | +0.0117 | +0.0541 |
| 47 | +0.0439 | +0.0230 | +0.0776 |

Against the inherited 0.05 floor: the gate as shipped clears **1/6**; the draw MEAN clears
**0/6**; the draw MAX clears **6/6**; a non-degeneracy floor on the draw SPREAD clears 6/6
trivially (sd 0.019-0.031 everywhere).

The substantive fact underneath: **the TYPICAL random rank-r subspace does not clear the
previous-action predictor on this substrate**, and on seed 45 it decodes BELOW it. 1043a's
single draw was, on 4 of 6 seeds, a LUCKY draw relative to its own reference distribution.
So "the comparator can move" is FALSE read as elevation and TRUE read as spread, and which
reading is pre-registered decides whether V3-EXQ-1043b adjudicates at all or refuses at
readiness exactly as 1043a did.

`D_comm` is nonetheless RESOLVABLE inside the reference distribution on every seed --
fraction of draws at or below 1043a's recorded `D_comm`: 0.58 / 0.04 / 0.04 / 0.50 / 0.00 /
0.00 -- i.e. the distribution is not degenerate and not saturated at either end.

## Result 4 -- adjacent finding: the fixed comparator does NOT make H1 resolvable at n=6

Recomputing the pre-registered H1 statistic (95% t-CI on the cross-seed C2 mean) with the
B=24 draw-mean comparator substituted for 1043a's single draw, against 1043a's recorded
`D_comm` (indicative, per the caveat above):

| comparator | per-seed C2 | mean | sd | 95% CI |
|---|---|---|---|---|
| 1043a single draw (as landed) | -0.014 +0.047 +0.042 +0.031 +0.091 +0.103 | +0.0500 | 0.0427 | [+0.0051, +0.0948] |
| B=24 draw mean | +0.002 +0.033 +0.041 +0.001 +0.087 +0.083 | +0.0409 | 0.0377 | [+0.0013, +0.0804] |

H1-small-but-real's declared null is "the CI EXCLUDES 0.05" (hypothesis registry,
`mech537_communication_subspace_orientation`). The de-noised comparator narrows the interval
but moves its centre DOWN, so the CI still excludes 0 and still includes 0.05 -- the same
undecided position 1043a landed in. The binding constraint is the CROSS-SEED sd (0.038), not
the draw noise the successor was designed to remove: at this mean and sd the CI's upper bound
first drops below 0.05 somewhere around n ~ 75 seeds. This is recorded because the autopsy
names "whether to spend it" as the user's decision, and it is directly material to that.

## What this probe does NOT settle

The formula and threshold for the re-specified readiness gate. That choice determines whether
V3-EXQ-1043b returns a verdict or refuses at readiness, which is a decision about the
criteria and about whether to run at all -- reserved for the user under the dispatch consent
rule. Raised as a decision chip; V3-EXQ-1043b is NOT queued and no driver was written.

Reproduce: `v3_exq_1043b_randrank_reference_smoke_20260920.py`, alongside this note. Set
`REE_V3_ROOT` / `REE_ASSEMBLY_ROOT` off the Mac defaults; needs a python with torch (~5 min,
2 cores). It OVERWRITES the JSON companion, so run it on a copy if the landed numbers matter.
