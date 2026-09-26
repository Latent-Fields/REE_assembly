# ASP gate (c) pre-registered seed extension under the decided env-truth-relative statistic (bt0926-aspext)

[chip_ref: chip-20260926-asp-gatec-seed-extension]

**User decision (2026-09-26):** extend seeds under the already-decided statistic; do NOT loosen the
gate. This record pre-registers the extension design (Part 1, committed BEFORE any new seed was
run), then reports the executed extension and verdict (Part 2, appended after the new seeds ran).

## 0. What this is extending

`gate_reread_user_decisions_20260926.md` (ee34814223, bt0926-decprobe) re-read ASP gate (c)'s
growth leg under the decided statistic -- predicted per-step growth (max over the model's own H=30
rollout, `max_growth_all`) <= 1.05x the environment's OWN TRUE per-step growth at the same held-out
state for the same first-action class the candidate took, PLUS the late-window (steps 21-30)
mean-growth bound (<=1.2) gate (e) already defines -- in the campaign preset (all 4 EMA reset-init
knobs ON). Result on seeds 106-110: **FAIL, 3/5 seeds** (106, 109, 110), mode-independent (both
ASP-E and ASP-0 fail on the same seeds), margins **0.7-2.4% over the env-relative bound** in every
failing cell -- a small, quantified gap, categorically different from the literal statistic's
61-79% (OFF-arm) miss.

**Unextended result, reported alongside per RULES point (iii):** 2/5 PASS, 3/5 FAIL on seeds
106-110 under the per-seed rule defined below. This is the baseline the extension is testing
against, not superseded by it.

## 1. PRE-REGISTRATION (committed 2026-09-26T15:3x Z, before seed 111 or any new seed ran)

**Code:** identical to `gate_reread_user_decisions_20260926.md`'s -- `ree-v3` tag
`archive/coupled-loop-repair-1b013d6` + cherry-pick `298cb8ffd3` (z_world reset-init) +
`bdfe901b37` (sibling z_self/shared/z_harm reset-init), in a fresh detached throwaway worktree
`/Users/dgolden/REE_Working/.scratch/wt-aspext/ree-v3-wt`. Both cherry-picks re-applied cleanly in
this worker's own worktree with **no conflicts**; independently re-verified diff shape (5 distinct
files touched across the two picks, since 3 overlap: `ree_core/latent/stack.py`,
`ree_core/utils/config.py`, `tests/test_flag_inertness.py`; +2 new contract test files) totalling
**632 insertions / 4 deletions**, matching the cited record's own **260+372 = 632 insertions**
exactly. Resulting sha stated by the source record: `5806a2be3349a1e753e8a68ee5217e1cc318bc43`.
No `ree_core` edits beyond the two cherry-picks (harness-only). Probe script reused byte-for-byte,
unmodified: `/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/decprobe/probes/decprobe/asp_gate_c_decided_probe.py`
(committed record: `gate_reread_user_decisions_20260926.md` sec 3). Same knobs (all 4 EMA
reset-init flags ON = campaign preset), same `n_states=20` (yields ~160-180 held-out states/seed
after early terminations, matching every prior record in this line), same MODES = (ASP-E
stratified, ASP-0 stratified_uniform), same per-seed AND rule below.

### 1a. Sample size: 5 new seeds, n=10 total

Seeds 106-110 are **kept in the final count, not discarded** (RULES point (i)). Five NEW seeds are
fixed here, before any of them is run: **111, 112, 113, 114, 115** (contiguous continuation of the
existing 106-110 numbering; chosen for no reason other than being the next unused integers in this
probe's seed sequence -- not cherry-picked for expected direction, since none has been run yet).
Total n=10.

**Why 5 new (not more, not fewer):** the existing 5-seed sample already gives an estimate of the
per-seed worst-mode excess ratio's spread (sd ~=0.0168, computed below in 1c) tight enough that
doubling the sample to n=10 is the smallest extension that materially sharpens the pooled test's
resolution (from being unable to distinguish "mean at the bound" from "mean below it" at n=5, to a
~1%-scale minimum detectable effect at n=10 -- see 1c). This matches the RULES' explicit steer
("recommend 5 -> n=10") and keeps the probe inside the ~2h Mac-CPU-lock-shared budget (5 seeds x
~250-400s/seed wall, per `run_all_seeds.log`'s measured per-seed times, well under an hour of
actual compute spread over holds respecting the 45s/15min protocol).

### 1b. Per-seed statistic and pass rule (UNCHANGED from the cited record)

Per seed, per mode (ASP-E, ASP-0): `pass_decided` = `gate_ratio_ok AND gate_growth_ok_decided AND
gate_late_ok` (unchanged bar and unchanged statistic, per RULES). **Per-seed pass = BOTH modes
pass_decided** (the AND rule the cited record already uses -- both modes have failed together on
every failing seed measured so far, so this is not a new bar, just restating the existing one).

**Per-seed scalar for the pooled test:** `e_i = max(excess_ratio_ASP-E_i, excess_ratio_ASP-0_i)`,
where `excess_ratio = pooled_max_growth_all / (1.05 x true_g1_first_class)`, i.e. the SAME decided
statistic, expressed as a ratio to its own bound (<=1 means the bound is met). **Worst-of-modes,
not both-modes-as-separate-points:** ASP-E and ASP-0 draw from the same held-out states and the
same trained head within a seed, so treating both as independent samples would be pseudo-replication
(the same failure mode the project's own E3-readout precedent already flags) -- one scalar per
seed keeps the n=10 pooled test's degrees of freedom honest.

### 1c. Pre-registered composite decision rule

Two components, BOTH pre-specified now, combined by AND (chosen over a bare majority or a bare
pooled test alone -- justification below):

**(A) Majority component.** Count of seeds (out of 10) whose per-seed pass (1b) is True. Majority-
PASS requires **>= 8/10 (80%)**, not a plain >50%. Justification: the existing base rate is 2/5
(40%) with all misses inside a 0.7-2.4% margin of the bound -- a coin-flip-adjacent regime. A plain
6/10 majority bar would let the extension flip PASS on noise alone (given the observed near-tie);
80% requires the five NEW seeds to swing clearly favourable (>=4/5 new seeds passing, combined with
the existing 2/5) before the count alone certifies a clean result.

**(B) Pooled-magnitude component.** One-sample, one-sided t-test on `{e_i - 1}` for i=1..10 (df=9),
H0: mean(e) >= 1 (bound violated on average) vs H1: mean(e) < 1 (bound met on average), alpha=0.05
(one pre-specified test, no multiplicity correction needed). Reject H0 (support PASS) iff
`t = (mean(e) - 1) / (sd(e)/sqrt(10)) <= -1.833` (one-sided critical value, df=9, alpha=0.05).
Using the 5 already-observed seeds as a pilot estimate of spread: mean(e)=1.0056, sd(e)=0.0168,
giving a projected minimum detectable effect at n=10 of **~0.97% below the bound**
(`1.833 x sd/sqrt(10)`) -- i.e. this test can resolve a true mean excess as small as ~1% either
side of the bound, which is the same order of magnitude as the margins actually observed
(0.7-2.4%). This is reported as a pre-registered power caveat, not tuned after seeing the new data.

**Combination and false-pass risk.** PASS only if **both (A) and (B)** indicate pass. FAIL only if
**both** indicate fail (majority <=5/10 AND t-test fails to reject with mean(e)>=1). **Any
disagreement between (A) and (B), or (B) failing to reject with the observed spread wider than the
~1% MDE computed above, is reported as CANNOT_DETERMINE**, not resolved in either direction --
because a disagreement between a count-based and a magnitude-based read of the same near-miss is
itself the finding (it says the extension did not resolve the ambiguity, not that it can be
adjudicated by picking whichever component happened to pass). Requiring AND (not OR) for PASS is
the conservative choice, matching the cited record's own framing of this as "close, not clean" --
an OR rule would let either component alone manufacture a PASS verdict, which is exactly the
false-pass risk this design is built to bound. The residual false-pass risk under AND is the
product-ish of: (i) component (A)'s risk that >=8/10 seeds pass by chance even though the true
per-seed fail rate is close to 50-60% (materially smaller than a bare 6/10 threshold's risk, by
construction); (ii) component (B)'s alpha=0.05 nominal Type-I rate, conditional on the t-test's
normal-ish-error assumption holding for excess ratios of this scale (not independently verified
here -- a stated limitation, not a gap papered over).

### 1d. What will be reported regardless of verdict

Per-seed excess magnitudes for ALL 10 seeds (both modes), so a reader can see directly whether the
misses are narrow noise scattered around the bound or a consistent small bias in one direction --
this is reported independent of which side of the pass rule the pooled test or majority count land
on.

---

## 2. EXECUTION AND RESULT (appended after seeds 111-115 ran; see git history of this file for the
pre-registration-only version committed first)

