# INV-109 endpoint-identity spike -- partial result, same-class repeat inconclusive at full scale

Chip: `chip-20260916-inv109-endpoint-hash-spike`. Campaign: `science-20260924-inv109-hash-spike`.
Pre-flight: AMBER (orchestrate-20260924-0808, 2026-09-24T10:57:01Z, ree-v3 main `44ddbfd`).
Ratified by: INV-109 proposal-track RED "not an EXQ" feasibility record (REE_assembly `90b0e626b45`).

**Status: PARTIAL. The named full-scale same-class-repeat identity test (two independent
full-scale reproductions, compared) was not completed.** One full-scale reproduction ran to
completion; a second was not attempted after the first took ~9.6h of pure compute (~13h
wall-clock end to end) on a severely CPU-contended shared box, and continuing into a second
multi-hour run was judged (by the orchestrating session, on resume) not to fit the chip's
operating window. What follows is the complete, honest record of what was measured, plus a
smaller-scale (dry-schedule) two-process comparison that is suggestive but not the named test.

## What INV-109 asks

INV-109 (`REE_assembly/docs/claims/claims.yaml`) asserts that re-running a documented training
recipe reconstitutes an operating REGIME and licenses nothing about the identity of the artifact
a prior run measured. Its 2026-09-15 disposition named the test: `hash_tensor_state` on two
reproductions of one recipe. The stated falsifier: bit-identical endpoints across machine
classes AND repeated runs would mean the commit pin already delivers endpoint identity and the
distinction has no operational content.

## Cross-machine half: already decided, cited not re-run (pre-flight point C)

Landed data already refutes the cross-class half of the falsifier as originally worded:
- V3-EXQ-1008 (ree-worker-3, linux-x86_64, commit `ceea428`) vs V3-EXQ-1010 (DLAPTOP,
  darwin-arm64, commit `63aa9f2`): `world_encoder_max_abs_delta` differs on all 3 seeds
  (0.28158509 vs 0.28158903, 0.29296178 vs 0.29300782, 0.36116445 vs 0.36116451), and OFF
  participation ratio differs too (4.56505 vs 4.56566, seed 42). Different endpoint weights ->
  different sha256 with certainty, so "hashes differ across machine classes" was already true.
- That comparison mixes machine class with a substrate-commit change and cannot separate the two.
  The only cell whose outcome was open going into this spike was the SAME machine_class + SAME
  clean commit repeat -- that is what this spike targeted.

## Design (per the AMBER pre-flight's named changes)

- **Driver**: `inv109_hash_spike_driver.py`, written to run OUTSIDE `ree-v3/experiments/` (in a
  throwaway `ree-v3` worktree, never committed to `ree-v3`), importing
  `v3_exq_1010_zworld_overcapacity_decoder_sweep._warm_off_agent` UNCHANGED. Because calling a
  driver's per-cell function directly (rather than through `x1010.run_cell`'s `main()` loop)
  bypasses the `with arm_cell(...):` wrapping entirely -- see `arm_fingerprint.py`'s 2026-09-17
  `chip-20260917-armcell-bypass-guard` docstring, which names exactly this shape as what
  invalidated V3-EXQ-1048's full-scale figures -- the driver calls `reset_all_rng(seed)` itself
  immediately before each agent-construction call, replacing what `_ArmCell.__enter__` would
  have done. This is a correctness fix for the direct-call shape the pre-flight's own named
  changes require, not a redesign.
- **Positive control** (Named Change B): the untrained agent's hash
  (`x1002._make_agent` right after `reset_all_rng(seed)`, no warmup) is captured alongside the
  warmed hash in every reproduction.
- **Scale**: full recipe = 60 P0a (SD-070 z_world encoder warmup) + 200 P0 + 90 P1 episodes x 200
  steps, the all-ON stack (`ree_allon`), seed 42 (one of `SEEDS = [42, 43, 44]` in
  `v3_exq_1010...py`, chosen to match the seed the pre-flight's cited participation-ratio figure
  used). Dry schedule (Named Change D) run first to smoke-test the driver at
  `DRY_RUN_P0/P1=2, STEPS=20` before committing to full scale.
- **Commit**: throwaway `ree-v3` worktree off `origin/main`, detached at `a62f00dd` (clean;
  avoids the dirty-checkout hazard the pre-flight named for the Mac's main checkout -- this
  box's main `ree-v3` checkout was independently clean and at the same commit, but the worktree
  was used anyway per the named change).
- **Threads/hash-seed pinning** (Named Change A): planned as unpinned-first, then
  `torch.set_num_threads(1)` + `PYTHONHASHSEED=0` as a second pair. Only the first unpinned
  reproduction was completed (see Outcome below); the second unpinned reproduction and both
  pinned reproductions were not run.

## Results

### Dry-schedule two-process comparison (smoke test, NOT the named full-scale test)

Two independent OS processes, same seed (42), same commit, unpinned (`torch.get_num_threads()=2`,
`PYTHONHASHSEED` unset), `DRY_RUN_P0=DRY_RUN_P1=2`, `DRY_RUN_ZWORLD_P0=2`, `STEPS=20`:

| | untrained_hash | warmed_hash | world_encoder_max_abs_delta | warm_elapsed_s |
|---|---|---|---|---|
| process A | `13b33715...92164dc` | `25427071...8aa38e7` | 0.008070811629295349 | 17.36 |
| process B | `13b33715...92164dc` | `25427071...8aa38e7` | 0.008070811629295349 | 16.58 |

Both hashes are **bit-identical** across the two independent processes, at dry-run scale.

### Full-scale reproduction (ONE only -- the second was not run)

Seed 42, unpinned, `torch.get_num_threads()=2`, `PYTHONHASHSEED` unset, Linux-5.15.0-191-generic
x86_64, torch 2.13.0+cpu, Python 3.10.12, ree-v3 commit `a62f00dd1ace131402eb5a7142fb09d1b5c72eed`:

```json
{
  "untrained_hash": "13b337151d270834b31844442eeba8e8d5703f018c80f4b18f74e699e92164dc",
  "warmed_hash": "7fabbed6fb950bfa967208e8d999769bb73b8f6dbc6d33af4d5ddf1a27bb339b",
  "warm_guard": {
    "n_world_encoder_tensors": 4, "n_world_encoder_changed": 4,
    "world_encoder_max_abs_delta": 0.2929617762565613,
    "zworld_encoder_trained": true
  },
  "warm_elapsed_s": 34711.75,
  "zworld_participation_ratio": 4.56505291002958,
  "zworld_train_rows": 5038
}
```

The `warm_elapsed_s` (34,712s = 9.64h) is the driver's own wall-clock measurement of the warmup
call alone (excludes process startup, the untrained-control construction, and the regime
readout). End-to-end PID lifetime was ~13h (see Timing below) -- the gap is queueing/contention,
not extra work.

**Untrained-agent hash** matches the dry-run pair's untrained hash exactly (identical across
THREE independent processes now: dry-A, dry-B, full-scale). This is expected -- the untrained
construction path (`reset_all_rng(seed)` + `x1002._make_agent`, no warmup) does not depend on
`DRY_RUN_*` scale at all -- but it is a genuine three-way confirmation that the instrument's
positive control is stable across independent processes on this box/commit.

**Warmed-agent hash** was captured once. There is no second full-scale warmed hash to compare it
against, so **the named same-class-repeat identity question is not answered by this run alone.**

**Regime readout**: `zworld_participation_ratio = 4.56505291002958` matches the pre-flight's
cited V3-EXQ-1008 (linux, commit `ceea428`) figure of `4.56505` to 5 decimal places, despite this
run using a different substrate commit (`a62f00dd`, materially later than either lineage run).
That is suggestive that this specific regime-level readout is stable within machine class across
commit drift -- consistent with the "regime readouts agree" half of INV-109's own framing -- but
it is a comparison against previously-landed data, not a second reproduction from this spike.

`world_encoder_max_abs_delta = 0.2929617762565613` falls within the range of the three
previously-landed cross-class deltas (0.28-0.36) and matches one of them
(`0.29296178`) to 8 significant figures; given the pre-flight's seed-to-delta correspondence in
its own prose is not fully unambiguous, this is reported as a data point, not a claimed exact
seed match.

### Timing and the resource premise this run corrects

The pre-flight already flagged "minutes of work" as false, re-measuring at "hours, not minutes."
This run shows that estimate was itself optimistic for the shared cloud lane: **34,712s (9.64h)
of pure compute for ONE full-scale warmup, ~13h wall-clock PID lifetime end to end**, on a box
that was running `load average: 5-7` on 2 cores for most of that window (other concurrent
metaworker sessions' experiment processes; confirmed via `ps aux` / `uptime` mid-run -- not a
defect in this driver). The originally-planned design (2 unpinned + 2 pinned full-scale
reproductions) would cost on the order of **40+ hours of wall time** on this class of shared
box, not the "hours" framing in the pre-flight or the chip's own prompt. That is a real,
re-measured premise correction, not a design change: the same-class-repeat test itself is
unchanged; only its true cost was wrong.

## Outcome (per the pre-flight's outcome map, point E)

**Not reached conclusively.** The map's two branches (`bit-identical` vs `differs while regime
agrees`) both presuppose a completed two-reproduction full-scale comparison, which this spike
does not have. The available evidence:

- Untrained-agent hash: identical across 3 independent processes (dry-A, dry-B, full-scale) --
  strong support that the instrument and this box/commit are well-behaved and deterministic for
  the no-training path.
- Dry-schedule warmed hash: identical across 2 independent processes -- suggestive, same
  direction as INV-109 predicts (same-class + same-commit repetition CAN reproduce
  bit-identically), but at ~1/17 the recipe's episode count and 1/10 the step count, not the
  named full scale.
- Full-scale warmed hash: one measurement only, nothing to compare it to from this spike.
- Regime readout (participation ratio) at full scale: matches previously-landed same-class data
  to 5 decimals across a commit change, supporting cross-commit regime stability independent of
  the hash question.

Reading the above together leans toward the same direction as the dry-run/untrained evidence
(same-class + same-commit repetition being reproducible), but this spike cannot state that as an
adjudicated finding at the scale INV-109's disposition specified.

**Git Re-Basin caveat preserved** (Ainsworth et al. 2023, cited in the 2026-09-16 literature pull
for INV-109): even a hash MISMATCH between two full-scale reproductions would only show
RE-DERIVATION was detected, not that the underlying model is SCIENTIFICALLY different --
permutation symmetry can make functionally-equivalent models hash differently. This spike's
partial evidence leans toward IDENTITY (not mismatch), so this caveat is not load-bearing for
the current record, but is stated for anyone extending this work.

## Same-day audit caveats (2026-09-25, checked against this run)

Per `REE_assembly` `08c6ed0c53` and its underlying census docs:
- **GFLAG-0491** ("no waking gradient learning at defaults"): under the all-ON recipe used here,
  E1 and E2-self are reported untrained at defaults. This spike does not touch E1 or E2-self; it
  targets the z_world encoder / latent_stack endpoint specifically (SD-070 P0), which this run's
  own `warm_guard` confirms trained (`zworld_encoder_trained: true`, all 4 world_encoder tensors
  changed, delta 0.293). Not invalidating, but stated for anyone reading this hash result as
  evidence about waking learning more broadly -- it is not.
- **GFLAG-0485** ("E2 world head has no native waking training objective... untrained in >=half
  of recent drivers"): per `gradient_reach_census_20260925.md`, the E2 world head IS trained
  under the all-ON recipe specifically (untrained only under the "1078 recipe" / native
  defaults). This run used all-ON, so this caveat does not apply to it, but is recorded for
  provenance since GFLAG-0485 is adjacent to (not the same as) the world_encoder/SD-070 path this
  spike measures.
- **SD-070 P0 precondition**: without it, the z_world encoder never trains. This run's schedule
  included `zworld_p0=60` episodes (`ZWORLD_P0_EPISODES`), and the resulting `warm_guard` confirms
  the precondition was satisfied.

## Named-changes compliance (pre-flight checklist)

- **A** (2 independent processes, same machine_class, same clean commit, unpinned then pinned):
  partially done -- ONE unpinned full-scale reproduction completed; the matching second unpinned
  reproduction and both pinned reproductions were not run (see Timing above). `torch_num_threads`
  and `PYTHONHASHSEED` recorded in every output regardless.
- **B** (untrained-agent positive control): done, in every reproduction (dry and full-scale).
- **C** (cite cross-class data instead of re-running): done, see above.
- **D** (dry schedule first, then one seed full scale; driver outside `ree-v3/experiments/`):
  done. Driver lives at `.scratch/ree-v3-spike-wt/inv109_hash_spike_driver.py` in a throwaway,
  uncommitted `ree-v3` worktree -- not landed to `ree-v3` (this is a spike, not an experiment; no
  `experiment_queue.json` entry, no `/queue-experiment`, per INV-109's own notes).
- **E** (outcome map): read as inconclusive at full scale; recorded above rather than forced into
  either branch.
- **F** (land only after the `/governance` hold on `evidence/planning/` releases): verified clear
  immediately before landing (`task_claim.py check --resources REE_assembly/evidence/planning/`
  and a scan of `TASK_CLAIMS.json` for any directory-scope claim on `REE_assembly/evidence/`
  found none active at landing time, 2026-09-25T01:2*Z).

## What this leaves open

Completing the named full-scale same-class-repeat test (the second unpinned reproduction, plus
the pinned pair) needs either a dedicated, uncontended box for roughly two more ~10h runs (and,
if pursued, two more ~10h+ pinned runs, pinning to `threads=1` likely costs MORE wall time than
unpinned since it removes intra-op parallelism on an already CPU-bound job) -- or a decision by
INV-109's owner that the dry-schedule + untrained-full-scale evidence already gathered here is
sufficient operational support for a disposition, without the full named design. That is a call
for whoever next works INV-109, not made here.
