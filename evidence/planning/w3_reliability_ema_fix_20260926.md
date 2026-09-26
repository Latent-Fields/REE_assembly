[chip_ref: chip-20260926-w3-reliability-with-ema-fix]

# W3 reliability with z_world EMA reset-init ON: LOWERS the pass rate (9/15 -> 1/15) -- not a disc4 regression, a k-collapse in the gate's OWN readout instrument

- **Status: MEASURED, paired re-run over the same 15 seeds (901-915) `w3_reliability_sweep_20260926.md` registered OFF. Verdict: LOWERS.** Session `bt0926-w3relon` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-w3-reliability-with-ema-fix`. Written 2026-09-26T08:05Z.
- **Question being closed:** does the z_world EMA reset-init fix (`zworld_ema_reset_init_build_20260926.md`, 3969d212ba) raise the W3 recipe's per-seed pass rate, applied ON for the whole pipeline (babble, training and readout), same 15 seeds and recipe as `w3_reliability_sweep_20260926.md` (b180ff7ee3f, 9/15 pass at post=1200).
- **Code:** `ree-v3` tag `archive/coupled-loop-repair-1b013d6` (the SAME tag `w3rel` used) with `main`'s `298cb8ffd3` (the SD-008 reset-init build) cherry-picked on top, in a detached throwaway worktree `/Users/dgolden/REE_Working/.scratch/wt-w3relon/ree-v3-wt`. **Result sha `5ff72ec7ba84decfe20e9a603230d0b06e665c0f`** (cherry-pick applied cleanly, no conflicts -- 4 files changed, 260 insertions, 0 deletions, identical diff shape to the one `gate_c_with_ema_reset_init_20260926.md` cherry-picked onto a different base tag). Worktree removed at the end. No `ree_core` edits beyond the cherry-pick. No queue, no chips beyond the one closed here, no `claims.yaml` edits.
- **Evidence domain: D1.** The quantity (a natively-trained head's disc4/k readout on held-out data) exists, moves, and is read directly; no consumer-mediated (E3/behaviour) intervention performed here.

## 1. Premises re-measured

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | the w3rel probe's OFF code path reproduces bit-exactly from this new worktree (canary) | Re-ran 2 of the 15 registered seeds (902, 904) with the knob explicitly `False`, full recipe, and diffed against the committed `W3REL_s{902,904}.json`: `post.disc4_h1`, `post.k` (both arms) and `B0` all MATCH to full float precision (abs diff 0, not merely `<1e-12`) for both seeds. | **holds, bit-exact** -- the cherry-picked worktree, RNG streams and this script introduce zero behavioural change with the knob OFF; the ON results below are trustworthy against the OFF baseline. |
| P2 | the knob must be set on BOTH `ref`'s config and each arm's training `agent`'s config to be live for the whole pipeline (gatec3's own pattern) | Followed `gate_c_ema_reset_init_probe.py`'s exact attribute path: `ref.latent_stack.config.use_zworld_ema_reset_init = bool(knob)` right after `R.build_B`, and `agent.latent_stack.config.use_zworld_ema_reset_init = bool(knob)` right after each `BB.fresh_agent` call (the B0 `pol_agent` and each arm's training `agent`). | **holds**, confirmed by the canary (P1): with knob explicitly `False` on both, behaviour is bit-identical to the pre-fix code, so the attribute path is wired correctly and inert when off. |
| P3 (brief's framing) | "does the fix raise the pass rate" presumes the fix's effect on THIS gate is well-approximated by its effect on disc4 alone (the axis the build record and gate (c) record both measured) | **Corrected.** The W3 gate is `disc4_h1 >= 0.47 AND k == 10` -- a conjunction. disc4 alone shifts in the HOPED-FOR direction under ON (mean +0.021, paired 95% CI `[0.007, 0.036]`, excludes zero), but `k` (a monotonic-streak count over `evaluate()`'s own persistence-vs-model-error comparison, unrelated to the disc4 threshold) collapses from its OFF-universal value of 10 to 0-7 in 14/15 seeds. The gate's `k==10` conjunct, which the OFF sweep found never bound (`w3_reliability_sweep_20260926.md`: "k = 10 in every row, so the bar is decided by disc4"), is what actually decides this result, and it is a readout-instrument confound, not a claim about the underlying mechanism. See sec 3. | corrected before the verdict was drawn, not silently. |

## 2. Design (reused byte-identically from `w3_reliability_sweep_20260926.md`)

Same 15 seeds (901-915), same recipe (`probes/w3rel/w3rel_probe.py`'s pipeline: babbling 2400 steps -> FROZEN retained set -> 3000 member updates (pre) -> 1200 native closed-loop `StepHarness` steps (8 updates/step, 25% retained mix, re-encoded) -> `evaluate()` on the held-out disc4/disc5 test set; SHUF twin with the fixed permutation). **The only change:** an optional `--knob` flag (`probes/w3relon/w3relon_probe.py`) that sets `use_zworld_ema_reset_init` on both `ref`'s config and each arm's training `agent`'s config before any `sense()`/`encode()` call -- knob live for the WHOLE pipeline (babble, training and readout), matching `gate_c_ema_reset_init_probe.py`'s own pattern. `--knob false` is the bit-exact canary (sec 1, P1); `--knob true` is the registered ON run.

**Primary:** pass rate ON vs OFF (OFF = the committed `w3rel` results), paired per seed, McNemar-style 2x2 counts. **Secondary:** mean disc4 delta (paired), B0 disc4 ON vs OFF, whether B0 disc4 still predicts the miss under ON. Gate (a) definition unchanged: `post disc4_h1 >= 0.47 AND k == 10` -- **the W3 bar was not changed.**

**Cost / stop rules followed:** MAC CPU LOCK discipline (>=800MB free+inactive, 2 threads), batched 1-4 seeds per hold (`~850s` internal budget per hold, self-stopping before the next seed once a hold's elapsed time exceeds that budget), 45s pause between holds, 6 holds total. Total probe wall time **~98 min** (smoke 195s + canary 392s + 5 ON batches: 887+1062+1148+928+1072+210 = 5307s), well inside the ~2.5h cap; no seed count reduction was needed (all 15 pre-registered seeds completed at the registered post=1200 dose).

## 3. Results

### Canary (P1): bit-exact

| seed | field | OFF (committed) | re-run (knob=False) | match |
|---|---|---|---|---|
| 902 | real post disc4_h1 / k | 0.50333... / 10 | 0.50333... / 10 | exact |
| 902 | shuf post disc4_h1 / k | 0.14333... / 10 | 0.14333... / 10 | exact |
| 902 | B0 | 0.33 | 0.33 | exact |
| 904 | real post disc4_h1 / k | 0.47 / 10 | 0.47 / 10 | exact |
| 904 | shuf post disc4_h1 / k | 0.11333... / 10 | 0.11333... / 10 | exact |
| 904 | B0 | 0.28333... | 0.28333... | exact |

### Pass rate (primary)

| arm | N | pass | rate | Wilson 95% CI |
|---|---|---|---|---|
| OFF (committed) | 15 | 9 | 0.600 | [0.357, 0.802] |
| **ON** | 15 | **1** | **0.067** | **[0.012, 0.298]** |

**McNemar 2x2 (rows=OFF, cols=ON):**

|          | ON-pass | ON-miss |
|---|---|---|
| **OFF-pass** | 1 | 8 |
| **OFF-miss** | 0 | 6 |

Net flips (OFF-miss->ON-pass minus OFF-pass->ON-miss) = 0 - 8 = **-8**. Every seed that passed OFF except one (915) flipped to miss under ON; no seed that missed OFF flipped to pass. Per the pre-registered verdict rule (RAISES needs net flips >= +3 with pass rate up; LOWERS is the symmetric case, pass rate down with a >=3-flip swing the other way) this is unambiguously **LOWERS**.

### Per-seed detail (real arm)

| seed | OFF disc4 | OFF k | ON disc4 | ON k | OFF pass | ON pass |
|---|---|---|---|---|---|---|
| 901 | 0.4567 | 10 | 0.4900 | 0 | False | False |
| 902 | 0.5033 | 10 | 0.5000 | 0 | True | False |
| 903 | 0.3900 | 10 | 0.4433 | 0 | False | False |
| 904 | 0.4700 | 10 | 0.5033 | 1 | True | False |
| 905 | 0.4967 | 10 | 0.5533 | 1 | True | False |
| 906 | 0.4567 | 10 | 0.4900 | 0 | False | False |
| 907 | 0.4767 | 10 | 0.4900 | 3 | True | False |
| 908 | 0.4900 | 10 | 0.4933 | 0 | True | False |
| 909 | 0.4333 | 10 | 0.4367 | 0 | False | False |
| 910 | 0.4633 | 10 | 0.4867 | 7 | False | False |
| 911 | 0.4467 | 10 | 0.5333 | 0 | False | False |
| 912 | 0.4900 | 10 | 0.4900 | 1 | True | False |
| 913 | 0.4733 | 10 | 0.4900 | 3 | True | False |
| 914 | 0.5367 | 10 | 0.5200 | 5 | True | False |
| 915 | 0.5367 | 10 | 0.5200 | **10** | True | **True** |

`k == 10` under OFF in **15/15** seeds (unchanged from the original sweep's own finding); under ON, `k == 10` in only **1/15** (seed 915). Guard PASS 15/15, FROZEN-retained-unchanged 15/15, rollout (e) bounded 15/15 under ON -- no anomalies. The A1 hazard stratum classification (901, 905, 908, 913, 914 = hazard-trapped) is identical between ON and OFF for all 15 seeds.

### Mean disc4 delta (secondary) -- moves in the HOPED-FOR direction, but does not decide the gate

Paired mean disc4 delta (ON - OFF), n=15: **+0.0213, 95% CI [0.0067, 0.0359]** (excludes zero -- a real, if modest, improvement). Range across seeds: -0.017 (914, 915) to +0.087 (911). **This is the opposite direction from the pass-rate result** -- disc4 alone would have suggested a mild RAISES, which is exactly why the conjunction with `k` matters here and must not be silently dropped from the readout.

### B0 disc4 (secondary)

Paired mean B0 delta (ON - OFF), n=15: +0.0142, 95% CI **[-0.0024, 0.0308]** (includes zero -- no reliable shift). "Whether B0 disc4 still predicts the miss under ON": **CANNOT_DETERMINE** -- only 1 of 15 ON seeds passes, so the pass-group has n=1 and Cohen's d is undefined (needs >=2 per group, same rule the original sweep's own predictor-separation analysis used for a 0/20 or 20/20 split). This is not evidence against B0's OFF-measured separation (d=1.227, `w3_reliability_sweep_20260926.md`) -- it is a sample-size artifact of ON's own near-total miss rate.

### Mechanism: why `k` collapses (D1, no extra probe run -- read directly from `evaluate()`'s own instrumented `err_over_pers_h1` field, already computed and saved by every seed above)

`k` (`babble_probe.evaluate()`) is a monotonic streak starting at horizon h=1: it only ever reaches 10 if the trained head's 1-step rollout error is BELOW the trivial "persist `x0`" baseline error (`err_over_pers_h1 < 1.0`) AND every subsequent horizon holds the streak. All 15 seeds show a uniform, large, one-directional shift in this ratio:

| seed | OFF err/pers @h1 | OFF k | ON err/pers @h1 | ON k | delta |
|---|---|---|---|---|---|
| 901 | 0.7202 | 10 | 1.0027 | 0 | +0.2826 |
| 902 | 0.7260 | 10 | 1.0009 | 0 | +0.2750 |
| 903 | 0.7252 | 10 | 1.0053 | 0 | +0.2801 |
| 904 | 0.7181 | 10 | 0.9894 | 1 | +0.2714 |
| 905 | 0.7211 | 10 | 0.9940 | 1 | +0.2728 |
| 906 | 0.6974 | 10 | 1.0121 | 0 | +0.3148 |
| 907 | 0.7579 | 10 | 0.9790 | 3 | +0.2212 |
| 908 | 0.7357 | 10 | 1.0121 | 0 | +0.2764 |
| 909 | 0.7695 | 10 | 1.0149 | 0 | +0.2454 |
| 910 | 0.7426 | 10 | 0.9812 | 7 | +0.2386 |
| 911 | 0.7097 | 10 | 1.0319 | 0 | +0.3222 |
| 912 | 0.7241 | 10 | 0.9771 | 1 | +0.2530 |
| 913 | 0.7231 | 10 | 0.9671 | 3 | +0.2440 |
| 914 | 0.7513 | 10 | 0.9902 | 5 | +0.2389 |
| 915 | 0.6692 | 10 | 0.9649 | 10 | +0.2957 |

Mean delta **+0.2688** (min 0.2212, max 0.3222 -- a tight, essentially seed-independent shift). Under OFF the ratio sits comfortably at ~0.67-0.76 (model clearly beats persistence); under ON it sits at ~0.96-1.03, right at the 1.0 boundary the streak requires. Seed 915 (the sole ON pass) has the lowest OFF ratio (0.6692, the most headroom) and lands at 0.9649 under ON -- just under the line; every other seed crosses it.

**Reading:** this is the same qualitative phenomenon `zworld_ema_reset_init_build_20260926.md` and `gate_c_with_ema_reset_init_20260926.md` already documented for the reset-init fix's OTHER first-tick-sensitive readouts (PR enrichment, gate (c)'s growth-leg bound) -- both those records explicitly flagged that a fix which makes z_world carry real, larger-magnitude information at/near a reset (rather than a near-zero collapsed signal) changes what "trivial persistence" costs, which can make an EXISTING FIXED-THRESHOLD readout instrument that was calibrated against the OLD, degenerate-near-reset regime look worse, even when the underlying representation is more informative (as disc4's own mild improvement here corroborates: classification-by-argmin over candidate actions gets slightly BETTER under ON, exactly what you would expect if z_world carries more distinguishing information near resets -- while the ABSOLUTE single-action rollout error at h=1, compared against a now-harder-to-beat persistence baseline, gets worse in relative terms). **This is not evidence that the fix breaks the world model** -- it is evidence that gate (a)'s `k==10` conjunct is calibrated against the pre-fix regime and does not transfer. Consistent with gate (c)'s own explicit warning ("experiments that compare first-tick behaviour across the fix are confounded") and with `w3_reliability_sweep_20260926.md`'s own observation that `k` never previously varied (so the W3 gate as originally built has NO evidence behind its `k==10` conjunct actually discriminating anything -- it was always 10, OFF).

## 4. Verdict

**LOWERS.** Pass rate 9/15 (0.600) OFF -> 1/15 (0.067) ON, Wilson 95% CIs [0.357, 0.802] vs [0.012, 0.298] (non-overlapping), net flips -8, unambiguous under the pre-registered rule. **The mechanism is fully attributable to a collapse in the gate's `k==10` readout conjunct** (mean err/pers@h1 shift +0.269, uniform across all 15 seeds), not to a regression in the underlying disc4 discrimination signal (which moves +0.021 in the OPPOSITE, hoped-for direction, CI excluding zero). Both effects are consistent with, and mechanistically continuous with, the reset-init fix's already-documented effect of making z_world carry real information near a reset instead of a collapsed near-zero signal.

## 5. Decisions the user/orchestrator owns (none taken here)

| id | decision | options |
|---|---|---|
| U6 (new) | Whether the W3 gate's `k==10` conjunct is still a meaningful pass criterion once resets carry real information (reset-init ON, or any other future change to the same z_world reset transient) | (a) Keep the gate as-is -- it was designed and measured under the pre-fix regime and this record shows it does not transfer; a future default-ON adoption of the reset-init fix would need `k`'s threshold or definition re-derived, not blindly re-applied. (b) Loosen or drop the `k` conjunct for any post-fix W3-family gate and re-decide reliability on disc4 alone (which itself moves in the hoped-for direction here). (c) Leave W3 gate untouched (per this brief's own instruction) and treat this record as informational input to the still-open U5 (`zworld_ema_reset_init_build_20260926.md`: default-ON is a user decision) -- a default-ON adoption would need this gate-transfer question settled first for any claim resting on W3's reliability. |
| U5 (inherited, unchanged) | Default-ON for `use_zworld_ema_reset_init` | This record adds: turning the knob ON, evaluated end-to-end against the EXISTING W3 gate, sharply LOWERS that gate's measured reliability -- but the decomposition above shows this is a readout-instrument artifact, not a finding that the fix degrades the underlying discrimination signal. Still not decided here. |

## 6. Not done

- Did not re-derive or propose a replacement `k` threshold/definition for the post-fix regime -- out of scope ("do not change the W3 bar").
- Did not run the DOSE probe (extending post beyond 1200) that the original sweep ran on its misses -- this record's misses are overwhelmingly `k`-decided, not disc4-margin-decided, so a dose extension would not plausibly move `k` back to 10 without first understanding whether the streak requirement is even the right instrument post-fix (sec 5, U6).
- Did not test whether a LOOSER `k` threshold (e.g. `k>=7`, which 910 and 914 already clear) recovers a pass rate closer to OFF -- that is a gate-redesign question, not this probe's (U6).
- Did not extend to `alpha_world >= 0.9` or to the sibling EMAs (z_self, z_beta/theta/delta) -- unchanged from every prior record in this line, out of scope per the brief.

Probe scripts: `probes/w3relon/w3relon_probe.py`, `probes/w3relon/analyze_paired.py`. Raw per-seed JSON: `probes/w3relon/results/` (not committed alongside -- scratch copy at `.scratch/breakthrough-20260924/w3relon/results/`).
