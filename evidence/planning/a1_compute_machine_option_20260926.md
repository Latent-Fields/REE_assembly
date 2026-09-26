# A1 compute: costing a larger cloud machine (PREPARE ONLY -- nothing provisioned)

- **Status: PLANNING / COSTING ONLY.** No server created, no queue edits, no config changes. Session `bt0926-a1mach` (`orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-a1-bigger-machine-costing`. Written 2026-09-26T18:21Z.
- **Purpose:** cost the user's option (decision 5, 2026-09-26) of a larger cloud machine for A1, for the user to weigh when A1 unblocks (W5 waits on V3-EXQ-1105b). Not a recommendation to buy anything now.
- **Inputs:** `a1_cost_remeasure_20260926.md` (`d602b030f3`, `d049d05809`: ~177 CPU-h ABSENT / ~205 CPU-h GROUNDED mid, 24+4 seeds), `coupled_a1_preregistration_draft_20260925.md` (arm/queue-item structure), `docs/reference/ree-v3-test-suite-routing.md` + CLAUDE.md "Running the test suite" (fleet mechanics -- a different workload, cited only where it transfers), live `hcloud` price/fleet queries (2026-09-26).

## 1. Premises re-measured before costing (per CLAUDE.md's stale-premise rule)

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | "A1 needs one big machine" implies vertical scaling helps | `experiment_runner.py:3429` docstring: a runner "is alive but will not claim a new item until its current run finishes" -- **one queue item at a time, per machine, full stop.** No N-parallel-jobs-per-box code exists anywhere in `experiment_runner.py`/`runner_remote_control.py` (grepped for `concurrency`/`parallel_jobs`/`max_concurrent`: zero hits) | **corrected.** The "cx43 (8 vCPU, 4 jobs)" framing carried over from `n2_replay_encoder_probe_20260925.md`'s Cost section is an **estimate of theoretical box capacity**, not a measurement against the production runner, which today gives a cx43 exactly the same concurrency (1) as a 2-vCPU box. A bigger machine does not multiply queue throughput under the current architecture -- see sec 3. |
| P2 | The existing fleet already includes an 8-vCPU worker, so "bigger" means beyond that | `hcloud server describe`: `ree-worker-3` (the fleet's only `cx43`, 8 cores/16GB) is already live and already in the general experiment pool, machine_affinity "any" | **confirmed, and load-bearing:** any new box is additive to a fleet that already has one 8-core member, not a first upgrade from all-2-core. |
| P3 | Fleet member types (unverified until this session) | `hcloud server list` + `server describe` (2026-09-26): `ree-worker-1` cpx22 (hub, no runner), `ree-worker-2` cpx22, `ree-worker-3` **cx43** (8 core), `ree-worker-4` cpx22 (surge/dual-role), `ree-worker-5` cx23 (resident, **no `ree-runner.service`** -- CLAUDE.md/memory confirmed, doesn't run experiments) | Usable experiment capacity today: worker-2 (2 core), worker-3 (8 core), worker-4 (2 core, surge-only). **3 machines, each running exactly one A1 item at a time regardless of core count** (P1). |

## 2. What actually determines A1's wall-clock time, given P1

A1 runs as **one queue item per admitted seed** (`coupled_a1_preregistration_draft_20260925.md` sec "Stage R": "one queue item per seed, `machine_affinity` any"), each item executing its full 16-18-arm set **sequentially inside one process**. With the runner's one-item-per-machine limit (P1), total wall-clock for the whole campaign is bounded by:

```
campaign_wall ~= ceil(n_items / n_machines) x per_item_wall(box_type)
```

**not** by any single box's core count, once that box is running a solitary item. `n_items` = 28 (24 admitted + 4 reserves per `a1_cost_remeasure_20260926.md` sec 8.4). `n_machines` today = up to 3 (worker-2, worker-3, worker-4-if-surging), **shared with the rest of the live experiment queue** -- A1 does not get exclusive use of them.

**A bigger single box changes `per_item_wall`, not `n_machines`.** Whether it helps depends on whether torch's *intra-op* thread pool (matmul/conv parallelism within one process) speeds up a single item on more cores -- unmeasured here, and a different mechanism from the "N concurrent jobs" framing this doc corrects in P1. The probes behind `a1_cost_remeasure_20260926.md` pinned `torch.set_num_threads(2)` deliberately (COMMON.md rule, to keep Mac probes small), so **no data exists on how A1's per-item wall scales past 2 threads** -- that scaling curve is the open measurement a real decision needs, not assumed here either direction.

## 3. Cloud-worker translation (ratio source restated, not re-derived)

Per `a1_cost_remeasure_20260926.md` sec 5, quoting `n2_replay_encoder_probe_20260925.md`'s Cost section: Mac 43 min/seed (a different, W3-dose workload) -> cpx22 (2 vCPU) estimated 5-7h, cx43 (8 vCPU) estimated 2-3h. Ratio: cpx22/Mac ~7.0-9.8x, cx43/Mac ~2.8-4.2x. **This ratio's cx43 side implicitly assumed 4-way concurrency (P1 says that concurrency does not exist in the runner today), so the cx43 number should be read as "if a single item ran alone on a cx43 with unrestricted threading," not "4x the throughput."** Applying it to A1's per-seed wall (`a1_cost_remeasure_20260926.md` sec 8.4, W4-ON, mid): ABSENT 6.27h, GROUNDED 7.28h Mac -> per item:

| box | vCPU | ratio (per item) | ABSENT mid | GROUNDED mid |
|---|---|---|---|---|
| cpx22 / cx23 (2 vCPU, existing worker-2/4/5-type) | 2 | 7.0-9.8x | 44-61h | 51-71h |
| cx43 (8 vCPU, existing worker-3) | 8 | 2.8-4.2x (unverified past 2 threads) | 18-26h | 20-31h |

28 items across 3 machines (best case, A1 gets the whole fleet to itself, which it will not in practice): roughly `ceil(28/3) x` the slowest of the three per-item numbers above -> **~10 batches x ~44-61h (cpx22-bound) ~= 440-610h (~18-25 days) if the 2 slower boxes gate it**, or, optimistically routing everything through the one cx43 first, `ceil(28/1) x 18-31h ~= 500-870h` on that box alone -- **either framing lands in the same 3-5-week calendar-time ballpark with the current 3-machine, one-job-each fleet, and none of it is improved by making one box bigger** (P1). This is the central finding: **the lever that shortens A1 is more machines each running the runner, not a bigger machine.**

## 4. Hetzner options actually costed (`hcloud server-type list` / `describe`, 2026-09-26, live prices, EUR/hr, fsn1/nbg1/hel1)

| type | cores | RAM | CPU class | EUR/hr | EUR/core-hr | note |
|---|---|---|---|---|---|---|
| cx23 (existing worker-5's type) | 2 | 4GB | shared | 0.0108 | 0.0054 | cheapest line |
| cpx22 (existing worker-2/4's type) | 2 | 4GB | shared | 0.0384 | 0.0192 | older "regular_purpose" line, 3.6x cx23's per-core price for the same core count |
| **cx43 (existing worker-3's type)** | 8 | 16GB | shared | **0.0315** | **0.0039** | already in the fleet |
| cx53 | 16 | 32GB | shared | 0.0582 | 0.0036 | 2x cx43's cores at ~the same per-core price -- cheapest way to add cores |
| ccx43 | 16 | 64GB | **dedicated** | 0.5440 | 0.0340 | ~9x cx53's per-core price for the same core count |
| ccx53 | 32 | 128GB | dedicated | 1.0517 | 0.0329 | ~9x per-core |
| ccx63 | 48 | 192GB | dedicated | 1.6824 | 0.0350 | ~9x per-core |

**The CX (shared, "cost_optimized") line is 9x cheaper per core than the CCX (dedicated) line at every size checked.** The existing fleet's worker-3 (cx43) and worker-5 (cx23) already use the cheap line; there is no evidence in hand that A1's workload is CPU-credit-throttled the way the pytest suite specifically was measured to be (`docs/reference/ree-v3-test-suite-routing.md`: "a bigger worker is NOT faster" for that suite, ree-worker-3 8 vCPU ran the *same single-threaded pytest run* ~1.8x *slower* than the 2-vCPU hub) -- that finding is about a single-threaded, burstable-credit-bound process, a different shape from A1's batched tensor ops, and does not transfer without a direct A1 measurement. Paying the ~9x dedicated-CPU premium is not justified by anything measured here.

## 5. Options table with a recommendation

| option | what it buys | EUR (compute only, whole A1 campaign) | calendar time | operational cost |
|---|---|---|---|---|
| **(a) Run A1 as ~28 queue items, `machine_affinity: "any"`, on the existing fleet** | Zero new infra. Competes with the rest of the live queue for worker-2/3/4's one-job-each slots | ~free (fleet already billed/scaled by the cloud-scaler for other work) | Slowest and least predictable -- A1 shares 3 slots with everything else already queued; see sec 3 for the un-shared-fleet floor (~3-5 weeks) | None -- this is what `/queue-experiment` already does by default |
| **(b) Spin up one temporary dedicated cx43 or cx53 for A1 only, `machine_affinity` pinned to it, torn down after** | A1 gets an exclusive slot that doesn't queue behind other work. Per P1, a cx53 is not faster per item than a cx43 unless intra-op threading past 2 threads measurably helps (open) | cx43: ~18-31h/item x 28 items = ~500-870 core-hours-of-wall-time x €0.0315/hr = **under €30 total**. cx53 same arithmetic, still **under €55 total** (both trivial in EUR) | ~3-5 weeks if run alone at 1 item/box regardless of size (P1) -- no better than (a)'s floor, only more *predictable* since nothing else contends for it | Provision + venv-match the hub's frozen `pip freeze` (per `docs/reference/ree-v3-test-suite-routing.md`'s resident-slot precedent) + `ree-runner.service` + one-off teardown after A1 closes. A real but small one-time chip. |
| **(c) Same as (b) but a CCX dedicated-CPU box** | Guaranteed (non-contended) cores, more RAM headroom | ~9x (b)'s EUR figure, still under €300 for the whole campaign -- trivial vs. the time cost, but buys nothing measured | Same as (b) under P1 -- no throughput win from more cores while the runner is one-job-per-machine | Not recommended: pays a 9x per-core premium against a workload shape (batched tensor ops, not single-threaded pytest) where the shared-vCPU throttling that justified CCX elsewhere has not been shown to apply |
| **(d) Build multi-job-per-machine support into the runner, then size a box** | This is the only lever that actually multiplies throughput (sec 2's `n_machines` term, not `per_item_wall`). A cx53 (16 vCPU / 32GB) sized at ~2 threads + ~4GB per job (matching the existing cx43/16GB : 4-job ratio implicitly assumed in sec 3) could plausibly host ~6-8 concurrent capped-thread runner instances once built | Same trivial EUR range as (b)/(c) for compute; the real cost is engineering, not hosting | Could cut the current 3-machine queue-sharing floor by roughly half to a third for A1 specifically | **Not a costing item -- a build item**, out of scope for this PREPARE-ONLY session and for "no provisioning." Named here because it is the actual answer to "how do I make this faster with money," which a bigger single box is not, today. |

**Recommendation for the user:** EUR is not the deciding factor anywhere in this table -- every option is under ~€300 for compute, several orders of magnitude below anything that would change the call. The real trade is calendar time vs. engineering effort:
- If A1 can share the existing fleet without urgency, **(a) costs nothing and needs no decision.**
- If A1 needs to not wait behind the rest of the queue, **(b) (one temporary cx43, cheapest line already in the fleet) is the lowest-effort way to get a dedicated, predictable slot** -- but per P1 it does **not** shorten the ~3-5-week floor, it only removes queue contention from that floor.
- **(c) is not recommended** -- it pays a large multiple for dedicated cores against an unmeasured (and, per the nearest measured analog, possibly absent) benefit.
- **(d) is the only option that actually shortens the campaign**, and it is an engineering task (runner concurrency), not a hosting purchase -- flagged for the user/`/queue-experiment` as the real next question if the 3-5-week floor is unacceptable, not decided or built here.

## 6. What this does not resolve (open, for whoever picks this up)

- Whether torch's intra-op thread pool gives a real per-item speedup past 2 threads on A1's actual op shapes (batch 32/64 forward+backward through E1/E2Self/W3/W6a/W1) -- no measurement exists in either direction; sec 2/3's cx43 ratio should be read as unverified past 2 threads until someone runs the paired-toggle-style comparison this repo already uses elsewhere (e.g. `a1_cost_remeasure_20260926.md` sec 8's paired-agent method) at 2 vs 4 vs 8 threads on one box.
- The real per-item wall on cloud hardware for the CURRENT W4-ON deployed config has never been measured on an actual cloud worker -- sec 3's numbers are Mac-measured x an extrapolated ratio from a different workload (`n2_replay_encoder_probe_20260925.md`), stated as such there and here.
- `/queue-experiment`'s open item O8 (`coupled_a1_preregistration_draft_20260925.md` sec 14) -- splitting each seed's item given the revised ~6-8h Mac / ~18-31h cloud per-item wall -- is unresolved and independent of the machine-size question this doc answers.

## 7. Reproduction

- Fleet facts: `hcloud server list`, `hcloud server describe ree-worker-{1..5}` (2026-09-26).
- Prices: `hcloud server-type describe {cx23,cpx22,cx43,cx53,ccx43,ccx53,ccx63}` (2026-09-26, fsn1/nbg1/hel1 rates; ash/hil/sin slightly higher, sin notably higher on traffic).
- Runner concurrency claim (P1): `ree-v3/experiment_runner.py` `_cloud_worker_is_available` docstring, line ~3429 on the checked-out `ree-v3` HEAD at claim time (no separate throwaway worktree needed -- read-only grep against the shared checkout, no execution).
