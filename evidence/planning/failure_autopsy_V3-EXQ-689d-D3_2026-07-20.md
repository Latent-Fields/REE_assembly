# Re-adjudication — V3-EXQ-689d defect D3 (`intra_run_substrate_divergence`)

**Generated** 2026-07-20T07:46:13Z · **Session** `musing-einstein-c80816`
**Supersedes** [`failure_autopsy_V3-EXQ-689d_2026-07-20`](failure_autopsy_V3-EXQ-689d_2026-07-20.md) (REE_assembly `2e6cc2569b`)
**Scope** `targets[0].defects[2]` (D3) **only**. D1 and D2 are not re-opened.
**Target run** `v3_exq_689d_mech448_f_eligibility_demotion_falsifier_20260621T063408Z_v3` · `V3-EXQ-689d` · MECH-448
**Trigger** [`intra_run_substrate_divergence_sweep_2026-07-20.md`](intra_run_substrate_divergence_sweep_2026-07-20.md) sec 3a, added after
[782](failure_autopsy_V3-EXQ-782_2026-07-20.md) / [604c](failure_autopsy_V3-EXQ-604c_2026-07-20.md) / [778a](failure_autopsy_V3-EXQ-778a_2026-07-20.md) refuted 3 of 3 SEVERE D3 routings.

> **One line.** D3 asserted that a mid-run `ree_core` edit on `DLAPTOP-4.local` confounded the
> treatment arm — an inference that carried an **unstated and unverified premise: that the edit
> reached execution.** It did not. Both hashes reconstruct byte-exact from committed trees; the two
> changed files are bound at the driver's **module scope** before the arm loop, in a single process
> with no dynamic imports; so all 12 cells executed identical bytecode. **D3 is REFUTED and
> WITHDRAWN.** 689d's withdrawal of `C_PRIMARY` **STANDS UNCHANGED** on D1 and D2, both of which were
> independently re-verified here and neither of which depends on D3.

---

## 1. What D3 claimed

`targets[0].defects[2]`, `sufficient_alone_to_withdraw: true`:

> "Arms execute in declaration order, so `ree_core` was edited on `DLAPTOP-4.local` between `ARM_ON`
> seed 42 and `ARM_ON` seed 43, while the run was in flight" ... "`C_PRIMARY` therefore has ZERO
> validly-controlled surviving seeds."

The observation is correct: 10 cells on `19b4073c`, `ARM_ON` seeds 43/44 on `fc6d17ce`, and the split
maps onto the finding exactly. The **inference** from that split to a loss of experimental control is
what is withdrawn. The original artifact characterises the change only as "of unknown content" — it
never asked whether the changed code could reach the running process.

## 2. Rung (a) — glob scope: the changed files ARE on the executed path

Unlike 782, this rung does **not** clear 689d. Both hashes reconstruct from committed trees:

| band | commit | committer date | n_files |
|---|---|---|---|
| `19b4073c` | `f53c28123eff` | 2026-06-20T19:48:43Z | 104 |
| `fc6d17ce` | `c15f84ee494f` | 2026-06-21T06:31:42Z | 104 |

Two globbed files differ, **both purely additive**:

```
 ree_core/agent.py        | 95 ++++++++++++++++++++++++++++++++++++++++++
 ree_core/utils/config.py | 33 +++++++++++++++++
 2 files changed, 128 insertions(+)
```

Both are on the driver's transitive static import closure (95 globbed files). So the D3 hit is **not**
a glob-scope artefact. Had the sweep's premise been sound, this would have been a genuine confound.

## 3. Rung (b) — process topology: the change never reached execution

This is the decisive rung, and it is the same mechanism that refuted 778a.

**The two changed modules are bound at driver module scope, before any loop:**

```python
# experiments/v3_exq_689d_mech448_f_eligibility_demotion_falsifier.py
128: from ree_core.agent import REEAgent          # noqa: E402
130: from ree_core.utils.config import REEConfig  # noqa: E402
```

`run_experiment()` opens its arm loop at line 1065 — **937 lines after both imports**. CPython caches
modules in `sys.modules` at first import, so `REEAgent` and `REEConfig` are the objects bound at
process start; the disk moving underneath them is invisible to the running process.

**Single process, verified structurally rather than by timing.** The driver contains no
`multiprocessing`, `Popen(`, `os.fork(`, `ProcessPoolExecutor`, or `joblib`, and no
`importlib` / `__import__` / `reload(` anywhere. All 4 arms x 3 seeds iterate in one `run_experiment()`
call. This matters because 689d's manifest is **missing per-cell `elapsed_seconds`** (an always-core
field the original autopsy already flags as absent), so 778a's elapsed/arm-count consistency check
**cannot** be run here. The structural argument replaces it and is in fact stronger: it does not
depend on timing at all.

**A restart is excluded by the hash pattern.** A runner restart would re-execute the run from the
start and stamp every cell with the new substrate; the observed pattern is 10 old / 2 new with exactly
**one** monotone transition in execution order. A restart is also excluded by the boundary falling
mid-arm rather than at a cell boundary the runner could resume from.

**Residual channel, and it is empty.** The one way a single-process run can still be exposed is an
**arm-conditional lazy import** — a module first touched only in a later cell, hence read from the
changed disk. Neither changed file is such a case (both are module-scope), and a scan of all 30
examinable divergent-run drivers found **zero** function-scope imports of `ree_core` or `experiments`
anywhere. `ree_core/agent.py` at the run-time revision contains no `importlib` / `__import__` /
`reload(` either.

**Therefore all 12 cells executed the `f53c28123eff` (`19b4073c`) substrate.** The hoisted per-run
`substrate_hash` would have been the correct identity for every cell — though 689d's manifest omits
that field entirely.

## 4. Rung (c) — not applicable, and why that is not a gap

604c's matched-pair test cannot run here: the boundary falls **within** `ARM_ON`, between seeds, so
there exists no pair of cells sharing a seed **and** an arm across the boundary. The available
cross-boundary seed-matched pairs are all *different arms* (`ARM_OFF` vs `ARM_ON`), which differ by
design — 3-5 of 25 fields identical, exactly as a real treatment effect should look. Their
non-identity is therefore **uninformative about substrate**, and must not be read as corroborating D3.
Rung (b) already settles the question without it.

## 5. D1 and D2 stand — independently re-verified

The user's instruction was to establish this explicitly rather than assume it either way.

**D2 (`vacuous_matched_noise_control`) — re-verified from the manifest here, and it is devastating.**
`ARM_PROPOSER_CTRL` and `ARM_MATCHED_NOISE` were compared field-by-field on all three seeds:

| seed | common fields | differing | `n_p1_ticks` |
|---|---|---|---|
| 42 | 27 | **`temperature` only** | 387 vs 387 |
| 43 | 27 | **`temperature` only** | 3616 vs 3616 |
| 44 | 27 | **`temperature` only** | 224 vs 224 |

26 of 27 fields bit-identical, including identical tick counts — identical trajectories. The only
differing field is the declared-but-inert knob itself. **They are the same arm.**
`MATCHED_ENTROPY_TEMPERATURE = 2.5` is folded into the fingerprint but never reaches a sampling step,
because `candidate_summary_source='proposer'` resolves by deterministic argmin. So the
"NOT noise-as-diversity" half of `C_PRIMARY` **never tested anything**, and the run PASSED only
because "strict above BOTH X and Y" degrades silently to "strict above X" when X == Y. This is
entirely independent of substrate identity and survives any DV repair.

**D1 (`hold_weighted_dv`) — `triage_class: DISQUALIFYING`, `survives_dv_repair: false`.** Not
re-opened here; nothing in this re-adjudication touches it. Both `selected_class_counts` and the
candidate histogram are hold-weighted (`agent.py:5430` / `:4812` return the held action and cached
candidates on `not ticks['e3_tick']`), the 663 calibration is excluded on two independently binding
grounds (entropy DV; up to **7.0x** asymmetric arm exposure within seed 42), and effective N falls to
~24-51 genuine selections against a 0.187-nat surviving margin.

**Conclusion: the withdrawal of `C_PRIMARY` stands.** D2 alone voids half the primary criterion, and
D1 alone disqualifies its DV. What is lost with D3 is only the specific "**zero validly-controlled
surviving seeds**" formulation — which was the sharpest phrasing but never the only ground. Anyone
citing 689d should now cite D1+D2, not D3.

## 6. Consequences beyond this run

**The class-origin claim is withdrawn.** 689d is where D3 was first "confirmed", and the corpus sweep
was commissioned from it. The sweep's headline base rate is re-derived in
`intra_run_substrate_divergence_sweep_2026-07-20.md` sec 3a-summary; **no run in the corpus now
survives the ladder as a demonstrated loss of experimental control.** D3 should be regarded as a
defect class that is **detectable but, on this corpus, never realised** — not as a disproven concern.
The mechanism is real; a subprocess-per-cell topology or an arm-conditional lazy import would realise
it, and neither is present here.

**What actually generalises from 689d is D2, and it is under-exploited.** "A control arm whose knob is
inert is bit-identical to its sibling, and a conjunctive criterion then degrades silently" is
mechanically detectable from any manifest — compare every declared-distinct arm pair for bit-identity.
That is a cheaper and higher-yield lint than the D3 divergence check, and it is recommended below.

## 7. Recommendations (proposed, not implemented)

`claims.yaml`, `review_tracker.json` and `substrate_queue.json` are **untouched**; `/governance`
applies these. **No manifest was edited** — completed runs are re-adjudicated via autopsy, never
rewritten.

1. **MECH-448: no change.** `evidence_direction` `non_contributory` and
   `epistemic_category: measurement_test_design_defect` both **retained**. The reading is unchanged;
   only one of its three supporting grounds is withdrawn.
2. **Re-derive brake: unchanged, MECH-448 remains 0.** This is shape **(c)** of the R1-R3 counting
   convention — direction and category retained, only supporting reasoning withdrawn — so this
   re-adjudication **supersedes** its predecessor rather than adding a hit (R2). R3 is not engaged:
   the category was never `substrate_ceiling`.
3. **The re-run spec is unaffected.** The original artifact requires the corrected re-run to fix the
   DV *and* defects 2 and 3. Requirement 3 (substrate homogeneity) is now moot for 689d specifically,
   but is harmless to retain as a general hygiene condition and should stay in the spec.
4. **Recommended new lint (from D2, not D3): `inert_arm_knob`.** For any multi-arm manifest, compare
   every pair of arms declared distinct; if two are bit-identical on all recorded per-cell fields
   except the knob that names their difference, emit a WARN. This would have caught 689d's D2 at
   write time. Cheap, purely manifest-local, no substrate dependency.

## 8. Limits

- **Scope is D3 on this run only.** D1 and D2 are re-verified, not re-opened; no other corpus run is
  adjudicated here (see the sweep sec 3a-summary for the corpus-level pass).
- **The import closure is static.** The dynamic-import scan returned zero on driver and `agent.py`,
  so the static trace is sound here — but per 782's caution this must be re-checked per run, never
  assumed.
- **The single-process argument is structural, not observational.** 689d records no per-cell
  `elapsed_seconds`, so there is no timing corroboration of the kind 778a had. The argument rests on
  the absence of process-spawning constructs in the driver plus the single monotone hash transition.
  A runner-level restart that somehow preserved 10 completed cells would defeat it; no such mechanism
  exists in the runner, which re-executes a claimed queue item from the start.
- **`DLAPTOP-4.local` attribution is unchanged and unimportant.** The edit did occur, on that machine,
  in that window. It simply could not reach the process.
