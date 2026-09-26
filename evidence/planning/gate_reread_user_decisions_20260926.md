[chip_ref: chip-20260926-gate-reread-under-user-decisions]

# Gate re-read under the 09:33Z decisions: W3 disc4-only RAISES (9/15->13/15) with the EMA fix; ASP gate (c) under the decided (env-relative) statistic is CLOSE but still FAIL-majority in the campaign preset, margins now single-digit-percent not 60-70% (bt0926-decprobe)

- **Status: MEASURED.** Session `bt0926-decprobe` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-gate-reread-under-user-decisions`. Written 2026-09-26.
- **Premise carried in from the brief, restated up front (per CLAUDE.md "audit its premises" rule): the 2026-09-26T09:33Z decisions this record applies are PROVISIONAL.** `coupled_loop_repair_campaign_plan.md` (`86d2b2d021b`) records that the user deferred to the orchestrator's recommendations without an informed choice ("I did not understand the implications well enough") -- these are orchestrator decisions under standing delegation, not user sign-off, and are explicitly flagged for revisit before A1 is queued. This record measures their CONSEQUENCES; it does not ratify them.
- **Question being closed:** re-read ASP gate (c) and the W3 member-gate reliability picture under decision (1) (env-relative growth statistic), decision (3) (W3 gate (a) = disc4 alone, k dropped) and decision (4) (all four EMA reset-init knobs ON in campaign probes).
- **Code:** ASP probe -- `ree-v3` tag `archive/coupled-loop-repair-1b013d6` + cherry-pick `298cb8ffd3` (z_world reset-init) + `bdfe901b37` (sibling reset-init: z_self/shared/z_harm) in a detached throwaway worktree `/Users/dgolden/REE_Working/.scratch/wt-decprobe/ree-v3-wt`. **Both cherry-picks applied cleanly, no conflicts** (result sha `5806a2be3349a1e753e8a68ee5217e1cc318bc43`; 4+4 files changed, 260+372 insertions, matching `gate_c_with_ema_reset_init_20260926.md`'s and `sibling_ema_reset_init_build_20260926.md`'s own diffs). Worktree removed at the end. No `ree_core` edits beyond the two cherry-picks. W3 reliability re-read (part A below) needed **no new code or compute** -- recomputed from already-committed/scratch per-seed JSON. No queue, no chips beyond the one closed here, no `claims.yaml` edits.
- **Evidence domain: D1** for both parts (quantities read/decoded from trained heads and, for part B, from direct environment instrumentation; no consumer-mediated (E3/behaviour) intervention performed here).

## 1. Premises re-measured

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | brief: "the disc4-only W3 pass rate may be computable from committed JSONs with NO new compute" | Recomputed `disc4_h1 >= 0.47` per seed directly from the raw per-seed JSON (`.scratch/breakthrough-20260924/w3rel/results/W3REL_s*.json` OFF, `w3relon/results/ON_s*.json` ON), not from the prose table alone. | **holds, exactly** -- no probe run needed for part A; see sec 2. |
| P2 | `w3_reliability_ema_fix_20260926.md`'s own finding: OFF `k==10` in 15/15 seeds, so gate (a)'s pass/fail was ALREADY disc4-decided before decision (3) | Re-derived: OFF disc4-only pass count (9/15) equals that record's own reported full-gate OFF pass count (9/15) exactly, seed-for-seed. | **holds** -- decision (3) changes nothing about the OFF baseline; its effect is entirely on how the ON arm is read (sec 2). |
| P3 | brief: "canary: with knobs OFF, the literal statistic must reproduce aspc's numbers (cbf0f87173) on >= 2 seeds" | Ran all 5 seeds (106-110), knobs OFF, literal `pooled_max_growth` (ASP-E/ASP-0, mode-independent as in every prior record): 1.7187/1.7385/1.7271/1.7132/1.7155 vs `asp_gate_c_readout_20260925.md`'s stored 1.719/1.739/1.727/1.713/1.716. | **exceeded**: matches to <0.001 absolute on all 5/5 seeds, not merely >=2. |
| P4 (new, this probe's own instrument) | whether the model's predicted per-step growth is step-1-dominated PER CANDIDATE, not only at the pooled level (the basis for using env-true STEP-1 growth as the "per-step growth" reference -- see sec 3 Method) | Checked directly: at the POOLED level (the single worst candidate across the whole pool), step-1 dominance holds exactly -- confirmed by P3's bit-for-bit reproduction of the OLD pooled statistic. At the PER-CANDIDATE level it does NOT hold universally: 51-100% of candidates (mode/seed-dependent) have their own local max_growth at a step other than 1, by a small margin (worst observed gap 0.024-0.111 across all 40 seed x arm x mode cells; see sec 3). | **corrected, not assumed**: the per-candidate approximation (comparing every candidate's own full-rollout max against its state's env-true STEP-1 growth) is a stated, quantified approximation, not an exact per-step reconstruction -- see sec 3's caveat. |

## 2. Part A: W3 member gate (a), disc4-only, fix OFF vs ON

**No new compute** -- recomputed directly from the raw per-seed JSON already committed/staged for `w3_reliability_sweep_20260926.md` (OFF, `.scratch/breakthrough-20260924/w3rel/results/W3REL_s{901..915}.json`) and `w3_reliability_ema_fix_20260926.md` (ON, `w3relon/results/ON_s{901..915}.json`), same 15 seeds, same recipe, `disc4_h1 >= 0.47` alone per decision (3).

| arm | pass | rate | Wilson 95% CI |
|---|---|---|---|
| OFF | 9/15 | 0.600 | [0.357, 0.802] |
| ON (all reset-init fixes) | 13/15 | 0.867 | [0.621, 0.963] |

Net flips: 4 seeds (901, 906, 910, 911) flip OFF-miss -> ON-pass; 0 seeds flip the other way. Per the pre-registered rule in `w3_reliability_ema_fix_20260926.md` (net flips >= +3, pass rate up = RAISES): **RAISES**, unambiguously.

**This directly inverts that record's own full-gate verdict (LOWERS, 9/15->1/15) by construction, not by new measurement of the mechanism.** That record already root-caused why: the `k==10` conjunct collapses under the fix (mean err/pers@h1 shift +0.269, a readout-instrument artifact of the fix making z_world carry real information at resets, not a regression in discrimination) while disc4 itself moves +0.021 (95% CI [0.007,0.036], excluding zero) in the hoped-for direction. Decision (3) drops exactly the conjunct that was driving the LOWERS reading. Both readings are correct for the gate definition they were computed under; only the gate definition changed.

## 3. Part B: ASP gate (c) under the decided (env-relative) statistic, all 4 EMA reset-init knobs ON

**Decided statistic (decision 1):** growth leg PASSES iff, for every candidate, the model's predicted per-step growth (max over the full H=30 rollout -- the same `pooled_max_growth` statistic every record in this line uses) is `<= 1.05 x` the environment's OWN true per-step growth at the SAME held-out state, for the SAME first-action class that candidate actually took, **plus** the late-window (steps 21-30) mean-growth bound gate (e) already defines (`<= 1.2`).

**Operationalisation (stated, not silent):** "env's true per-step growth" is read as the env's true STEP-1 growth (via `encode_next_side_effect_free`, the I1 instrument from `w3_step1_spike_attribution_20260925.md`, independently re-validated here: instrument max|diff| = 0.0 on 159-171 validated states per seed, 5/5 seeds), per candidate's own first-action class. Justification: the POOLED max growth is step-1-dominated in every prior record and reconfirmed bit-for-bit here (P3 above). **Caveat, re-measured not assumed (P4):** at the per-candidate level, 51-100% of candidates have their OWN local max at a step other than 1 -- but the magnitude of that deviation is small (worst gap 0.024-0.111 across all 40 cells), so this is a stated approximation with a quantified, small blind spot, not an exact per-step comparison. Per-candidate scoring: `excess_ratio = candidate_max_growth / (1.05 * true_g1[state, candidate_first_class])`; gate PASSES iff every candidate's `excess_ratio <= 1` (pooled max `<= 1`), AND the ratio leg ([0.5,2] median) and late-window leg (`<=1.2`) both hold.

**Code + method:** `probes/decprobe/asp_gate_c_decided_probe.py` (committed alongside this record). Reuses `gate_c_probe.py`'s (aspc) training recipe (E2WorldMember only, no codec) and CEM-pool generation for ASP-E/ASP-0, and `u3_step1_attribution_probe.py`'s env-replay-and-branch method (`gen_policy_env`), extended to all 5 action classes per state (u3 computed it for its own per-class table already; here it is needed per-candidate since ASP-E/ASP-0 candidates span all 5 first-action classes by construction). All four knobs (`use_zworld_ema_reset_init`, `use_zself_ema_reset_init`, `use_shared_ema_reset_init`, `use_zharm_ema_reset_init`) set on BOTH `ref`'s and the training agent's `latent_stack.config` before any sense()/encode() call, matching `gate_c_with_ema_reset_init_20260926.md`'s pattern extended to all four. Run TWICE per seed (knobs OFF canary, knobs ON = campaign preset), seeds 106-110, n_states=20 (166-179 held-out states/seed after early terminations, matching every prior record). Total wall time 1500s (~25 min) across 5 seeds, both arms, well inside the ~2h cap. **MAC CPU LOCK note:** the wrapper script had a bug (`rmdir` on a non-empty lock dir silently failed after cleanup, since the `owner` file inside was never removed first) that caused the shared lock to appear held long after each seed's compute had actually finished (~250-374s/seed, not 30+ min) -- flagged live by the coordinator, fixed in the script for the record, but the already-running process could not pick up the file edit (and could not be killed per instruction / permission policy), so the remaining seeds ran under the original both-arms-per-hold granularity rather than one-arm-per-hold; each individual hold's real compute stayed short (max 374s) and the coordinator cleared the resulting stale locks so `n3post` was not durably blocked.

### Literal (OLD) statistic, for context -- all 4 knobs vs z_world-only

| | OFF mean | OFF range | ON mean | ON range |
|---|---|---|---|---|
| `gate_c_with_ema_reset_init_20260926.md` (z_world ONLY, native pools) | 1.7384 | 1.696-1.794 | 1.1574 | 1.082-1.214 |
| **this record (all 4 knobs, ASP-E/ASP-0 pools)** | 1.7226 | 1.713-1.739 | **1.0501** | **1.028-1.074** |

With all four knobs ON, the ASP pool's literal-bound mean excess over 1.05 closes from 0.673 (OFF) to 0.0001 (ON) -- **~100% closed on average**, versus the z_world-only fix's 84% on the native pools. The three sibling knobs add real, further closure beyond z_world alone. Individual seeds still vary (1.028-1.074): 2/5 seeds (107, 108) literally PASS (`<=1.05`) with all four knobs ON; 3/5 (106, 109, 110) still fail, by 1-7%, not 60-79%.

### Decided statistic -- per seed, both arms (ratio leg PASSES 5/5 seeds x 2 arms x 2 modes throughout, unaffected)

| seed | OFF excess (E/0) | OFF decided pass (E/0) | ON excess (E/0) | ON decided pass (E/0) |
|---|---|---|---|---|
| 106 | 1.016 / 0.999 | F / **T** | 1.024 / 1.022 | F / F |
| 107 | 0.982 / 0.991 | **T / T** | 0.987 / 0.987 | **T / T** |
| 108 | 1.028 / 1.006 | F / F | 0.987 / 0.988 | **T / T** |
| 109 | 1.062 / 1.056 | F / F | 1.016 / 1.012 | F / F |
| 110 | 1.039 / 1.034 | F / F | 1.013 / 1.007 | F / F |

Late-window leg: always PASSES (max 1.017-1.075 across every seed/arm/mode, comfortably under 1.2, matching every prior record).

**Pass counts (decided statistic): OFF 2/5 (ASP-E), 3/5 (ASP-0); ON 2/5 (ASP-E), 2/5 (ASP-0).** Neither arm reaches 5/5. In the campaign preset (all 4 knobs ON, decision 4), gate (c)'s growth leg under the decided statistic is **FAIL-majority (3/5 seeds), mode-independent**, but by a small, quantified margin in every failing cell (excess ratio 1.007-1.024, i.e. 0.7-2.4% over the env-relative bound) -- categorically different from the literal statistic's OFF-arm failure margin (61-79% over bound) and closer to, but still short of, a clean pass.

## 4. Verdict

**Part A (W3 disc4-only): RAISES.** 9/15 -> 13/15, Wilson CIs [0.357,0.802] -> [0.621,0.963] (overlapping but both directionally clear), net flips +4/-0. Decision (3) (drop `k`) converts the earlier full-gate LOWERS finding into RAISES purely by removing a conjunct that record's own mechanism analysis showed was a readout artifact, not a discrimination regression.

**Part B (ASP gate (c), decided statistic, campaign preset = all 4 knobs ON): FAIL (majority, 3/5 seeds), both ASP-E and ASP-0, by a small quantified margin (0.7-2.4% over bound in every failing cell).** Neither the OFF nor the ON arm reaches 5/5 under the decided statistic -- this is a **CLOSE, not clean, result**: the decided statistic is a much narrower gap than the literal one (which fails 5/5 in every prior OFF reading, and still fails 3/5 literally even with all 4 knobs ON), but it is not a PASS. Canary (P3) and the instrument validation (P1 in `w3_step1_spike_attribution_20260925.md`, re-validated here to max|diff|=0.0) both hold at the strongest level measured. The per-candidate step-1-dominance approximation (P4) is a stated, small (<=0.11), non-silent limitation on how tightly "the decided statistic" was operationalised here -- a literal per-step (not per-candidate-max) re-implementation was out of scope for this probe's budget and was not needed given the small measured gap.

## 5. Decisions the user/orchestrator owns (none taken here)

| id | decision | options |
|---|---|---|
| U7 (new) | Whether "FAIL-majority by a small margin" is close enough to treat gate (c) as provisionally cleared for the campaign preset, or whether the residual 3/5-seed failure (0.7-2.4% over the env-relative bound) still blocks W1-alt/INT-ACT | (a) treat as effectively passed given the margin is within plausible measurement/seed noise (not measured here: no seed-noise floor was established for the decided statistic specifically); (b) hold gate (c) open and treat this as evidence the env-relative statistic needs a small slack term or a different aggregation (e.g. median-of-seeds rather than worst-seed) before being load-bearing; (c) revisit once the sibling-EMA default-ON decision (U5, inherited) is itself decided, since sec 3's literal-statistic table shows the four-knob config is already the best-measured configuration for this pool. |
| U8 (new) | Whether the per-candidate (not just pooled) step-1-dominance approximation (P4) needs a literal per-step true-growth re-implementation before gate (c) is treated as fully closed, given the measured gap is small (<=0.11) but nonzero | not decided here; the gap's practical effect on THIS record's PASS/FAIL calls was checked to be negligible (excess ratios move by less than the measured gap in every borderline cell) but a rigorous per-step version was out of scope. |
| U1, U5, U6 (inherited, unchanged) | see `asp_gate_c_readout_20260925.md`, `gate_c_with_ema_reset_init_20260926.md`, `w3_reliability_ema_fix_20260926.md` | this record narrows U1's practical stakes further (literal excess now 1-7%, not 60-79%, with all 4 knobs) but does not resolve which statistic is authoritative; U5/U6 (default-ON for the reset-init knobs, and the W3 `k` conjunct's post-fix meaning) remain open, revisit-flagged per the 09:33Z decision log's own provisional-status note. |

## 6. Not done

- No re-derivation of a genuine literal per-step true-growth comparison (P4's caveat) -- the measured gap was small enough not to change any PASS/FAIL call in this record, but this was checked, not assumed to be immaterial for all possible future uses of this instrument.
- No consumer-mediated (D2/E3) reach check -- unchanged from every prior record in this line, out of scope per the brief.
- No re-run of the OFF arm at n_states beyond 20, or of seeds beyond 106-110 for part B (matches every prior ASP record's seed set, per the brief's REUSE instruction).
- ASP-R (refit) not measured here -- brief scoped this to ASP-E and ASP-0 only, per decision context; ASP-R is a pinned strict xfail on gates (b)/(d) regardless (`asp_gate_c_readout_20260925.md`).
- The wrapper-script lock-hold bug (sec 3) is reported here as a finding, not fixed upstream in any shared skill/script -- it lives only in this session's throwaway `run_all_seeds.sh`, not a shared file.
