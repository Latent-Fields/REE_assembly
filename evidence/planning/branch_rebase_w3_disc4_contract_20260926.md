[chip_ref: chip-20260926-branch-rebase-w3-disc4-contract]

# ree-v3 integration/coupled-loop-repair rebased onto main (SD-008 reset-init knobs) + W3 gate (a) contract made disc4-only

- Session `bt0926-brrebase` (`orchestrate-20260924-breakthrough-c2`), written 2026-09-26T09:54Z. Test-only change on the branch; no `ree_core` edit, no queue, no registry edit.
- **New branch head: ree-v3 `integration/coupled-loop-repair` = `4070b0efa4`** (pushed with `--force-with-lease` against the head seen, `1b013d6`; never to `main`).
- **Pre-rebase head archived:** tag `archive/coupled-loop-repair-1b013d6` (already existed and was already on origin, tag object `37f88e1356` -> `1b013d6`; not re-created).

## 1. Rebase

- `origin/integration/coupled-loop-repair` (`1b013d6`, 5 commits over merge-base `07b5fe688d`) rebased onto `origin/main` = `bdfe901b37` (carries `298cb8ffd3` z_world reset-init and `bdfe901b37` sibling z_self / shared / z_harm reset-init knobs, all default OFF).
- **No conflicts.** The two overlapping files (`ree_core/utils/config.py`, `tests/test_flag_inertness.py`) auto-merged. Checked rather than assumed: `git range-diff` maps all 5 branch commits `=` (patch-identical: ASP `29f6e9c`, W1 codec `b47275e`, W3 `fbfb6fa`, W6a `03387e2`, W4 `73cb658`); `git diff 1b013d6 73cb658 --stat` equals `git diff 07b5fe688d origin/main --stat` exactly (9 files, +1925/-29), i.e. the rebase added main's delta and nothing else; the four `use_*_ema_reset_init` knobs appear in `config.py` / flag-inertness with the same counts as on main, and all 33 branch config field names keep the branch's counts.
- Targeted contracts on the rebased tree (`73cb658`), cloud route (`remote_pytest.sh`, hub, run_id `DLAPTOP-4-74613-20260926T094257Z-55088179`): ASP, W1 codec, T1 members, W2a structured babbling, W3, W6a, W4, `test_zworld_ema_reset_init.py`, `test_sibling_ema_reset_init.py`, `tests/test_flag_inertness.py` -> **196 passed, 2 xfailed** (the pinned strict xfails), 0 failed.

## 2. W3 contract change (commit `4070b0efa4`, `tests/contracts/test_w3_e2_world_member.py` only)

Decision implemented: coupled plan decision log 2026-09-26T09:33Z (REE_assembly `45d9c1d83f` + `86d2b2d021`; provisional/revisable) -- W3 member gate (a) = `disc4_h1 >= 0.47` ALONE; the `k == 10` conjunct is dropped as reset-artefact-carried (`w3_k_excluding_reset_ticks_20260926.md`, `370c222e20`; GFLAG-0560).

- New helper `_w3_gate_a(res)` = `verdict == PASS and disc4_h1 >= L2R_BAR`. (`coupled_acceptance.action_discrimination`'s own `verdict` was already disc4-only; the `k` conjunct lived only in the test's explicit asserts, so `experiments/_lib` needed no change.)
- W3-10: the real head must pass `_w3_gate_a`; the shuffled twin must still have `verdict == FAIL` and must NOT pass `_w3_gate_a` (the twin assertion kept, now on the disc4 bar alone). `k` is printed as a non-gating readout.
- W3-10b (new, pins the decision): a synthetic fixture (8-d, `z_{t+1} = z_t + E[a_t]`, a predictor exact for 2 steps then drifting) with `disc4_h1 = 1.00`, `k = 2` PASSES gate (a); its first-action-permuted twin (`disc4_h1 = 0.07`, `k = 0`) does not (non-vacuity). The fixture asserts `k == 2` so it cannot silently become k-complete.
- **Test half** (`.scratch/breakthrough-20260924/brrebase/test_half.py`, direct call, <1 s): with the PRE-change predicate (`verdict PASS and disc4 >= bar and k == 10`) swapped in for `_w3_gate_a`, W3-10b FAILS (old gate on the fixture = False); with the new gate it PASSES. The twin fails both gates.
- Post-change run (cloud, run_id `DLAPTOP-4-81176-20260926T095140Z-2002614794`): W3-10 and W3-10b PASSED; readout real `disc4_h1 0.687, k 10`, twin `0.213, k 10` (the twin also has k = 10 -- a live illustration that k does not discriminate the real map from a permuted one here).
- The ree-v3 pre-commit contract gate self-gates on `ree_core/**` / `experiments/_lib/**`; this commit stages neither, so the gate is a no-op for it and the Mac lock was not taken. The cloud runs above are the verification.

## 3. What this does not do

- Does not re-score any past W3 / N2 / N3 result under the new gate; plan rows citing "(a) 4/5 (... k 10 on 5/5)" stay as recorded.
- Does not change A1's R2 wording ("W3 gate (a) holds on the held-out test set") -- it inherits the new definition by reference.
- The deferred t>=8 persistence criterion (own threshold + null control) is not built.
