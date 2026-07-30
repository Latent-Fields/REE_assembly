# Stash triage + recovered manifest -- ree-cloud-4, 2026-07-30

**Triaged:** 2026-07-30T06:55Z -- 07:30Z, session `awesome-mestorf-fa7072`
(chip `chip-20260730-cloud4-stash-triage`)
**Source:** `ree-cloud-4` (hcloud `ree-worker-4`, 91.99.68.94),
`~/REE_Working/REE_assembly` (6 stash entries) + `~/REE_Working/ree-v3` (0 entries).

Third and final worker in the fleet sweep, after [`README.md`](README.md) (ree-cloud-3,
2026-07-29) and [`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md)
(ree-cloud-2, 2026-07-30). **`ree-cloud-4` is surge-mode / manual-start only and had never
been examined** -- it was powered off during both prior triage sessions. The hub
(`ree-cloud-1`) probes clean. With this, every fleet worker has been swept.

The worker was powered on for the triage and **powered back off afterwards** (it was off at
session start). No experiment was running; the runner was never stopped.

---

## Headline: the cloud-2 shape repeats, and the recovered file closes the 2026-05-30 cluster

**All 6 stashes are fully contained on `origin/master` -- zero ABSENT-ON-ORIGIN across
6 (stash, path) pairs.** As on cloud-2, the only genuine loss was an untracked `.bak`
manifest in the working tree that a stash-only triage would have missed entirely.

The recovered file is **`V3-EXQ-614`** -- the *third* member of the 2026-05-30
manifest-pipeline silent-drop cluster. Its two siblings were `V3-EXQ-490h` (recovered from
ree-cloud-2 on 2026-07-30, the previous session) and `V3-EXQ-592b`. **Both recoverable
members of that cluster have now been recovered, from two different workers, on two
consecutive days, and both were declared unrecoverable by the same autopsy.**

And because the successor was a **bit-identical re-run**, the recovery yields something
neither prior recovery did: a true replicate pair, which **disagrees**. See
"The reproducibility finding" below -- that, not the file itself, is the load-bearing
result here.

---

## Containment grading -- all 6 (stash, path) pairs

All 6 stashes were archive-tagged **by SHA, in one pass, before anything was touched**
(`stash-archive/20260730-<short-sha>`, local-only on the worker; `stash@{N}` is racy
because the runner rewrites the list every ~62s). Tags survived a reboot and remain
ref-reachable, therefore prune-immune:
`git -C ~/REE_Working/REE_assembly tag -l 'stash-archive/*'` (6).

| Grade | Pairs | Meaning |
|---|---|---|
| SEMANTIC-IDENTICAL | 5 | same parsed JSON as origin |
| CONTENT-DIFFERS | 1 | benign -- governance-applied `evidence_direction`, see below |
| ABSENT-ON-ORIGIN | **0** | -- |

Every entry held exactly **one** untracked flat manifest in `^3`, and no tracked paths.

| stash | date | manifest | grade |
|---|---|---|---|
| `a89b5cab2e` | 2026-07-29T22:23Z | `v3_exq_839_sd084_midexec_reachability_20260729T220727Z_v3` | SEMANTIC-IDENTICAL |
| `82996f807c` | 2026-07-29T18:34Z | `v3_exq_836c_mech476_novelty_tagging_consolidation_20260729T181956Z_v3` | CONTENT-DIFFERS |
| `53f0fbe2cb` | 2026-07-29T17:21Z | `v3_exq_837_mech475_distributional_critic_iatrogenic_falsifier_20260729T141738Z_v3` | SEMANTIC-IDENTICAL |
| `b817e97f3e` | 2026-07-28T20:30Z | `v3_exq_835_mech068_consolidation_selectivity_ablation_20260728T201442Z_v3` | SEMANTIC-IDENTICAL |
| `e952dcd804` | 2026-07-26T16:30Z | `v3_exq_793a_sd049_arm2_competence_repower_20260724T123828Z_v3` | SEMANTIC-IDENTICAL |
| `1efe9a1651` | 2026-07-24T12:40Z | `v3_exq_786b_mech163_dual_system_recruitment_20260724T123825Z_v3` | SEMANTIC-IDENTICAL |

### The single CONTENT-DIFFERS is benign

`82996f807c` / 836c: `stash_only=[]`, and the sole changed key is `evidence_direction`,
moving from the runner's raw self-route to the governance-applied verdict:

| | value |
|---|---|
| stash | `mixed` |
| origin | `non_contributory` |

Origin also carries the explaining `evidence_direction_note` ("the entire reversal is
attributable to one outlier seed in the unpaired arm; removing it flips the sign to a small
paired-favouring delta well inside the 0.15 margin"). Origin is the reviewed, authoritative
copy; the stash holds the strictly staler pre-review raw. Exactly the pattern that accounted
for all 11 CONTENT-DIFFERS on cloud-2.

### Mechanism: cloud-2 shape, not cloud-3 shape

Each of the 6 entries holds a **different** manifest, captured on 6 separate occasions
between 2026-07-24 and 2026-07-29 when a `git pull` failed all three retries and fell
through past `experiment_runner.py:1039` without ever calling
`_postpull_restore_prepull_stash()`. There is **no stuck recurring file**, so the ree-cloud-3
durable fix (remove it) does not apply. Object store is healthy and gc has never been
blocked:

- `git count-objects -vH`: 7282 loose / 62.02 MiB, in-pack 816504, `garbage: 0`
- **no `.git/gc.log`**

`ree-v3` on this worker: 0 stashes, 0 untracked, no tracked modifications.

---

## The recovered manifest

### `v3_exq_614_mech341_p3_behavioural_falsifier_3arm_20260529T191318Z_v3.json`

Recovered from
`evidence/experiments/v3_exq_614_..._v3.json.bak.20260530` -- **untracked in the working
tree, not in any stash**. Byte-identity verified on both sides with `git hash-object`:
`431460e1129168c9c32ae97063f269e85bc89b98`. The `.bak.20260530` suffix is the *same
cleanup event* that produced cloud-2's 490h backup.

- `V3-EXQ-614`, **FAIL**, `evidence_direction: weakens`, claims **MECH-341** + **ARC-065**
- 15 top-level keys; complete `result` block with `acceptance_criteria`,
  `decision_rule_thresholds`, `interpretation_grid` and full per-arm / per-seed data
- 3 arms x seeds `[42, 43, 44]`, 9/9 seeds completed; `experiment_purpose: evidence`
- `interpretation_label: FAIL_no_criterion_routes_to_diagnose_errors`
- No `machine` field (the schema of the day); ran on ree-cloud-4, inferred from location
- Coordinator DB: `experiments.status = completed` (updated_at 2026-05-29T19:13:19Z),
  **zero** `results` rows -- the positive stranded signature. All five lettered siblings
  (614a..614e) have a `results` row.
- `origin/master`: **no 614 path at all**. Origin carries 614a/b/c/d/e, not the base run.

**This is the third member of the cluster autopsied in
[`failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30`](../failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md)**,
absorbed into it at 2026-05-30T06:42:23Z. That autopsy records at line 20:

> "Filesystem: no manifest at `REE_assembly/evidence/experiments/v3_exq_614_*` (verified
> `find` returns nothing matching `*614*` under either flat path or `runs/`)."

That `find` was correct about the paths it searched and never reached ree-cloud-4's disk,
where the file had already been renamed to `.bak.20260530`. The same autopsy's
"per-condition acceptance metrics are unrecoverable" premise is now falsified for **two** of
its three members: 490h (recovered 2026-07-30 from cloud-2) and 614 (here). **592b remains
genuinely unrecoverable** -- it ran on `DLAPTOP-4.local`, and the previous session confirmed
the Mac holds no copy.

---

## The reproducibility finding -- the actual result of this triage

> **RESOLVED 2026-07-30, same day, by session `great-hopper-1d7b24` (chip
> `chip-20260730-arm2-allon-nonreproducibility`): the nondeterminism hypothesis below is
> FALSIFIED, and the open admission decision below is TAKEN. See
> [`RESOLVED_arm2_allon_nonreproducibility_2026-07-30.md`](RESOLVED_arm2_allon_nonreproducibility_2026-07-30.md)
> (REE_assembly `95a6021fb1`, `ec44fc414b`).**
>
> `ARM_2_ALL_ON` did not fail to reproduce. `ree-v3 a45ca7f` (2026-05-29T23:41:55Z) raised
> `e3_diversity_entropy_lambda` **0.05 -> 0.5** *between the two runs* -- 4h28m after 614
> finished, and 7h before the 614a driver was even authored (`ree-v3 c90ee9f`). **614 and
> 614a are not a replicate pair**; the FAIL -> PASS flip is the intended effect of that
> retune. The arm-localisation reasoning below is correct and its conclusion is explained
> without nondeterminism: MECH-341 is inert in `ARM_0` (A off -> pool collapses to one
> first-action class -> `apply_entropy_bonus` returns zeros *before* lambda is read) and not
> built in `ARM_1` (B off), so `ARM_2` is the **only** arm in which MECH-341 is live and
> therefore the only arm lambda can touch.
>
> Why the `config_summary` check below could not catch it: the driver pins
> `entropy_bias_scale` (recorded, unchanged) but **not** `entropy_lambda`, which is absent
> from `config_summary` entirely. **No reproducibility probe was queued** -- the hypothesis
> was closed documentarily at zero compute cost.


`V3-EXQ-614a` is **not an amended experiment**. Its own driver docstring states:

> "Bit-identical script body to V3-EXQ-614; only EXPERIMENT_TYPE / QUEUE_ID / SUPERSEDES
> constants + this docstring header change. claim_ids unchanged (MECH-341 + ARC-065) -- the
> science is identical; only the pipeline bug was the difference between predecessor and
> successor."

Verified by direct diff of the two drivers in `ree-v3/experiments/`: **35 diff lines, all of
them the docstring header, three constants, and one added manifest key.** The executable
body is identical.

So 614 and 614a are a **true replicate pair of a deterministic experiment** -- same
bit-identical script, same seeds `[42, 43, 44]`, same `config_summary` (verified
field-for-field identical), same `decision_rule_thresholds` (all 8 identical), same
`p0_episodes=30` / `p1_episodes=60` / `steps_per_episode=200`. Until now only one half of
that pair existed on origin, so the comparison had never been possible.

**They disagree, and the disagreement flips the verdict:**

| | 614 (stranded) | 614a (landed) |
|---|---|---|
| `C1_R2c_b_only_rung1` | false | false |
| `C2_b_necessity_delta` | **false** | **true** |
| `C2_entropy_delta_value` | **0.054043** | **0.157923** |
| `C3_all_on_rung1` | true | true |
| outcome | **FAIL** (`weakens` both claims) | **PASS** (`supports` both claims) |

The `necessity_entropy_delta` threshold is 0.1, so C2 crosses it and nothing else moves.

**The divergence is confined to a single arm.** A recursive structural diff of the whole
`result.arms` block yields 43 leaf differences, and **every one of them is in `arms[2]`**:

- `ARM_0_B_only` -- **bit-identical** across the two runs
- `ARM_1_ablate_B` -- **bit-identical** across the two runs
- `ARM_2_ALL_ON` -- diverges throughout (tick counts, class counts, entropies);
  `mean_selected_class_entropy_na` 0.579882 -> 0.683762, `n_seeds_rung1_pass` 2 -> 3

Since C2 is the necessity delta between `ALL_ON` and `ablate_B`, and `ablate_B` is
bit-identical, **the entire FAIL -> PASS flip is carried by the one arm that does not
reproduce**.

**Why this is unlikely to be a machine-class artifact.** 614 ran on ree-cloud-4 and 614a on
ree-cloud-3 (both `linux-x86_64`), so the known cross-machine-class `torch.multinomial`
divergence (which is `darwin-arm64` vs `linux-x86_64`) does not obviously apply. More
decisively: if the two boxes computed differently, all three arms should drift. Two of three
reproducing **bit-identically across the two machines** is strong evidence that the boxes
agree numerically and that `ARM_2_ALL_ON`'s divergence is intrinsic to that arm -- it is the
only arm with all four substrate axes on (`A_sp_cem`, `B_mech341`, `C_noise_floor`, `D_vs`),
so a nondeterminism reachable only in the full-stack combination is the natural hypothesis.

**This is not established here and this session did not investigate it.** What is
established is that the load-bearing PASS which routed MECH-341 to
`PASS_C2_C3_only_mech341_load_bearing_in_stack_only` rests entirely on an arm that a
bit-identical re-run did not reproduce. **That warrants a governance look and a
reproducibility probe; both are chipped, neither is taken here.**

---

## Open decision -- TAKEN 2026-07-30 (see the RESOLVED banner above)

> **ADMITTED with `evidence_direction: "superseded"`** (REE_assembly `ec44fc414b`), flat +
> `runs/<run_id>/manifest.json`. Measured fully inert: MECH-341 and ARC-065 `claim_evidence`
> field-for-field identical, `conflict_ratio` 0.0 -> 0.0, gap-register and
> promotion/demotion rows identical, `pending_review` unchanged at 9. The reasoning below is
> sound and was followed, with one refinement: `superseded_by_substrate` (+ `weakens`) was
> **rejected** despite being the semantically apt field, because it leaves
> `evidence_direction: weakens` and the gap register does not honour `scoring_excluded` --
> it would have minted both claims' first-ever conflict (MECH-341 0.0 -> 0.286). Recorded
> as `superseded_by_substrate: MECH-341@2026-05-29` *alongside* `superseded` instead.

### Original framing (retained)


**Whether to admit the 614 manifest as evidence is a governance decision.** The file is
parked here, **outside `evidence/experiments/`**, precisely so the indexer
(`build_experiment_indexes.py`, which scans
`evidence/experiments/{*.json, */*.json, **/runs/**/manifest.json}`) cannot silently score
it and move MECH-341 / ARC-065 confidence without a governance pass.

Points for whoever takes it:

- Per the EXQ supersession policy in `CLAUDE.md`, a superseded predecessor should be
  admitted with `evidence_direction: "superseded"`, which the indexer treats as inactive.
  On that treatment it would move **no** claim confidence.
- Admitting it as-emitted (`weakens`) would be the error -- it would mint scored `weakens`
  entries for MECH-341 and ARC-065 out of what the cluster autopsy already classified as a
  **delivery failure, not a scientific FAIL**.
- The stronger argument for admitting it is **provenance, not evidence weight**: it is the
  only record that the falsifier returned FAIL on its first execution, which is the fact the
  reproducibility finding above rests on.

## Also preserved (no evidence value, kept rather than judged)

`sd037_consumer_input_distributions_20260531T175254Z.md` and
`..._20260601T180611Z.md` -- human-readable distribution reports written into
`evidence/planning/` by runs `V3-EXQ-620` and `V3-EXQ-620b`. Both are absent from
`origin/master` by path, but **both parent runs are fully landed** (flat manifest + pack +
metrics), and the landed manifests carry the same numbers at higher precision in
`cohort_summary.rows[].per_quantity` and `pooled_summary`. Spot-verified: the `.md`'s seed-42
`z_harm_a_norm` row (min 0.3158 / max 0.3328 / mean 0.3231 / std 0.0035 / p70 0.3247 /
p90 0.3281) matches the landed manifest's 0.3157801330089569 / 0.3328230679035187 /
0.323079343352999 / 0.0034774484945457925 / 0.32468525171279905 / 0.3281471490859985 exactly
at 4dp, and the pooled p70 0.4326336085796356 matches the report's 0.4326. These are derived
renderings of landed data, **not stranded evidence**. Retained only because nothing is
dropped on a judgement call. The analogue of cloud-2's `_per_tick.jsonl` finding.

Two further untracked `.json` files on the worker
(`v3_exq_794_...` and `v3_exq_794a_...`, duplicated inside their experiment subdirectories)
graded SEMANTIC-IDENTICAL to the flat form on origin. Contained; left in place.

**No untracked working-tree file was deleted on this worker.** Only the 6 contained stashes
were dropped, by SHA, each verified against its archive tag with the list re-resolved on
every iteration.

---

## Operational note: the scaler powers this worker off mid-triage

A triage session creates no queue claim, so to `cloud-scaler.py` the woken worker is
indistinguishable from an idle one. **The first power-on of this session was shut down
~2 minutes in**, before any work completed -- the same failure the pytest lease was built
for (`read_lease()`, ree-v3 `fc0ee74024`).

Fix used, and the one to reuse for any future worker triage: take the lease **before**
power-on, renew it while working, release it at the end.

```bash
ssh ree@91.98.130.117 'mkdir -p /home/ree/pytest_leases && cat > /home/ree/pytest_leases/ree-cloud-4.lease' <<EOF
{"expires_at": "<now+29min ISO8601 Z>", "owner": "...", "purpose": "stash_triage"}
EOF
```

Expiry is clamped to 30 min by `PYTEST_LEASE_MAX_MIN`, so it must be renewed for a longer
session and cannot strand a billing VM if the holder dies. `read_lease()` fails safe in
every direction. Released at end of session; worker powered off.

## Related

- [`README.md`](README.md) -- ree-cloud-3 (2026-07-29), the method this follows
- [`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md) -- ree-cloud-2
  (2026-07-30); source of the "grade the untracked working tree, not just the stash list"
  lesson that found the only real loss here too
- [`../failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md`](../failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md)
  -- the cluster autopsy whose "unrecoverable" premise is now falsified for both 490h and 614
- [`../ree_v3_orphaned_autostash_triage.md`](../ree_v3_orphaned_autostash_triage.md) --
  archive-tag convention and containment method
- `REE_assembly/scripts/runner_git_health.py` -- reports stash **counts** only; it cannot
  tell a contained stash from a stranded one, and does not look at untracked files at all
