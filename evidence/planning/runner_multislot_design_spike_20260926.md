# Runner multi-slot design spike: N queue items concurrently per machine (DESIGN ONLY)

- **Status: DESIGN / OPTIONS ONLY.** No code, config, queue or fleet change was made. Nothing was measured on the live fleet. Session `suspicious-jackson-2d8021`, chip_ref `chip-20260926-runner-multislot-design-spike`. Written 2026-09-26T18:35Z.
- **Origin:** `a1_compute_machine_option_20260926.md` (REE_assembly `7eedfa1ce4`), P1. It found that the runner claims one queue item per machine, so a bigger box does not speed up A1 (~177-205 CPU-h). The user called multi-item-per-machine "genius, though it may run into its own problems". This document inventories those problems and lays out the options. **It decides nothing.**
- **Code baseline:** `ree-v3` HEAD `8e41454` (= origin/main at 2026-09-26T18:13Z). Every file:line below is against that sha. The critical lines were re-read by hand, and the rest came from three read-only inventory passes.

## 0. Premises re-measured (CLAUDE.md premise-audit rule)

| # | premise (from the brief / A1 doc) | re-measured | verdict |
|---|---|---|---|
| P1 | The runner claims one item per machine (`experiment_runner.py:3429` docstring) | Docstring at `:3426-3432`. The mechanism is deeper than that docstring: the main loop (`:5407` `while True` -> `:5465` `for item` -> `:5653` blocking `run_experiment`) is synchronous, and the main thread IS the child's stdout pump (`:4747` `for line in proc.stdout`). `_current_claim` and `_current_proc` are declared "0 or 1 elements" (`:5169`, `:5174`). No concurrency, slot, pool or `max_concurrent` code exists anywhere in the runner. | **confirmed, and it is structural, not a config limit** |
| P2 | "Slots beat threads" is the unmeasured deciding premise | Nothing in the runner, `ree_core`, `experiments/_lib`, `ree-runner.service` or `shadow.conf.*.example` sets `torch.set_num_threads` / `OMP_NUM_THREADS` / `MKL_NUM_THREADS`. `_build_subprocess_env` (`:4255-4283`) adds only `REE_QUEUE_ID`, `REE_RUNNER_SIGNAL_DIR` and `REE_QUEUE_DECLARED_SEED_COUNT`. **Today one item on the cx43 already runs at torch's default of 8 threads, and on a cpx22 at 2.** Only 2 production scripts pin threads (`v3_exq_1021...py:482` sets 1, `v3_exq_1108...py:158` sets 2). | **sharpened.** The question is not "do we add threads". It is whether K items at 8/K threads each beat 1 item at 8 threads, which the fleet runs today. Still unmeasured (sec 3). |
| P3 | The coordinator must be taught to allow >1 claim per machine | `try_claim` (`coordinator/db.py:3731-3791`) has **no per-machine claim count**, so a second claim by the same machine on a different item already returns `ok`. | **corrected.** The claim is not the blocker. Everything *around* the claim is keyed on one machine name with one `current_exq` (sec 1.2). |
| P4 | Thread count is already controlled or recorded, so reproducibility is a new slot-only hazard | `machine_class()` (`experiments/_lib/arm_fingerprint.py:134-167`) = platform-arch-python-torch. It has **no thread count** and no `num_threads` field is stamped anywhere. The fleet already runs `machine_affinity: any` items at 8 threads (cx43) and 2 threads (cpx22) indiscriminately. | **corrected.** Thread count is **already an unrecorded run variable** today. Slots make it worse only if left unpinned. |

## 1. Inventory: every one-item-per-machine assumption

### 1.1 Runner (`ree-v3/experiment_runner.py`, 6212 lines; `runner_remote_control.py`; `coordinator_client.py`)

**Control flow and process state**
- `:5` module docstring: "Runs pending experiments ... sequentially". `:4341` `run_experiment` docstring: "Run a single experiment script as a subprocess".
- `:5407` / `:5465` / `:5653`: `while True` -> `for item in items` -> blocking `run_experiment(...)` inside `with _substrate_freeze(queue_id)`. `:4747` `for line in proc.stdout` runs on the main thread.
- `:5169` `_current_claim  # 0 or 1 elements`. Set at `:5641-5642`, cleared at `:5672`/`:5675`.
- `:5173-5179` one runner-wide set of flags: `_drain_flag`, `_current_proc` (0 or 1, `:5174`), `_pause_flag`, `_suspend_flag`, `_resume_run_target`, `_force_stop_flag` and `_sigint_force_armed`. `proc_ref` is filled at `:4568-4570` and cleared at `:4945-4947`.
- `:5679-5701`: one SUSPENDED result drains the whole runner. `:5477-5493`: `_resume_run_target[0]` is a single target.
- `:6059-6149` between-pass work (result push, idle heartbeat, sleep, ree-v3 pull `:6109`, version refresh, V3-parity gate `:6117`, self-restart `:6129`, peer merge, queue reload). The comment at `:6119-6126` says it assumes "no claim is held and no experiment subprocess is alive". **With continuously overlapping slots, that moment never comes.**
- Self-restart: `:1645-1672` `_self_restart_busy_reason` checks `current_claim[0]` / `current_proc`. `:1829` `os.execve` replaces the process and would orphan any live child. `:1514-1520` "BETWEEN EXPERIMENTS ONLY".
- `_substrate_freeze` (`:2348-2391`) already tolerates multiple holders, because tokens are `{pid}-{uuid}.json` (`substrate_freeze.py:307`). But `_substrate_freeze_blocked` (`:2313-2345`) would defer ree-v3 pulls **indefinitely** while any slot holds a token.
- Module globals, one per process: `:1423-1424` runner version, `:1909-1910` parity gate state, `:446` git-corruption state. `:3873` `_write_status_lock` is `threading.Lock`, so it covers this process only.

**Machine identity used as the key**
- `:3346-3354` `_get_machine_name` = `canonical_machine_name(--machine or hostname)`, resolved once at `:5094`. `ree-runner.service:62` runs one unit per box with `--machine <m>`.
- `:4981-4987` the `--machine any` help text claims it disables affinity filtering. **This is not implemented** (`_affinity_matches` would compare against the literal "any"). It is a latent doc bug, not slot-specific.
- Claim / release: `:3734` `coordinator_client.claim(queue_id, machine)` (`coordinator_client.py:133`); `:3765` `release_claim(queue_id, machine)` (`:150-151`).
- Legacy git-mode `attempt_claim` `:3592-3676`: `:3630-3632` lets the same machine re-claim its own claimed item. **Two slots sharing a name could double-claim one item in git mode.** `release_claim` at `:3701` lets any same-name process release a sibling's claim.
- Heartbeat: `:4598-4619` `_push_remote_heartbeat(... current_exq=item["queue_id"], progress=..., runner_pid=os.getpid())`. Idle heartbeat at `:6088-6102`, startup at `:5137-5141`, final `offline, current_exq=None` at `:5196-5227`. **One exiting slot would blank the row for its siblings.** Payload at `runner_remote_control.py:219-246`; `coordinator_client.py:169-170` sends `{machine, state, current_exq, progress, gpu}`.
- Status: `:6012-6017` `report_status(machine, full_status)`. The status dict (`:4231-4240`) has one `current` and one `runner_pid`.
- Shutdown: `:5186-5187` `/shutdown_notify {machine}` with reasons `runner_signal_exit` (`:5232`) and `runner_drain_complete` (`:6200`).
- Remote-control commands are addressed to a **machine**. In `runner_remote_control.py:1261-1339`: `stop` sets the global drain, `force_stop` kills `current_proc[0]` only (`:1288-1302`), `pause`/`resume` are global, and `suspend` sets one flag. `kick` and `release_claim` take `args.queue_id` but arrive on the machine channel. The mid-run poll is restricted to `{suspend, force_stop}` (`:131-141`) precisely because `release_claim` against "the CURRENTLY RUNNING item" was a hazard, which assumes a single running item. `_process_git_command_file` (`:1366-1378`) is an unlocked read-modify-write, so N pollers would double-execute.

**Affinity and laptop yield**
- `:3357-3365` `_affinity_matches` = `"any"` or `same_machine` (exact after canonicalisation). The coordinator mirror is `db.py:3253-3269` `_affinity_ok`.
- `:3372-3377` `LAPTOP_YIELD_CLOUD_HOSTS` is hard-coded to cloud-1..4. `:3418` `_AVAILABLE_CLOUD_STATES={"idle"}`. `:3421-3454` `_cloud_worker_is_available` requires `state=="idle"` and no `current_exq`. **Availability is binary per machine: a box with a free slot but one busy slot counts as "unavailable".**

**Exit handling**
- `:5735` `_transient_exit_codes={137,-9,-11,-15,143}` applies to the single `result`, releases one claim (`:5753`) and sets `status["current"]=None`.
- `:5251-5298` `handle_signal`: a second SIGINT kills `_current_proc[0]` only; `_do_immediate_exit` (`:5229-5249`) releases only `_current_claim[0]` and flips every running queue entry back to pending.
- The systemd default `KillMode=control-group` means SIGTERM reaches every child. That is fine for slots.

**Stale-claim observers (runner side, observability only)**
- `:3793-3852` `recover_stale_claims` skips own-machine claims (`:3834`). `:3503-3536` `_claim_owner_has_fresh_heartbeat` requires `hb.current_exq == queue_id` (`:3530`).

**Progress**
- `:4747-4849` parses per-call closures (fine per slot). They feed one `status["current"]` (`:4495-4520`) and one heartbeat. `:4757` `print(line)` would interleave N children in `runner.log`.

**On-box files that would collide (N processes on one box, or N pumps in one process)**
- `runner.pid` (`:106`, written at `:5166` with **no single-instance guard**).
  - **Existing defect, not slot-specific:** `--dry-run` rewrites `runner.pid` at `:5166` and unlinks it at `:5356`, deleting a live runner's pid file. `REE_assembly/serve.py:228` reads that file.
- `runner_status/<machine>.json` (`:3857-3866`, fixed `.tmp` at `:3917`) and monolithic `runner_status.json` (`:4049`, `:4133-4137`).
- `runner_heartbeats/<machine>.json` and `runner_commands/<machine>.json` (`runner_remote_control.py:216-217`, `:1025-1026`).
- `experiment_queue.json` via `_atomic_write_queue` with a **fixed** `experiment_queue.json.tmp` (`:3584`), and read-modify-write removal at `:5842-5845`, `:5911-5914` and `:6040-6043`.
- `script_timing.json` (`:108`): `save_script_timing` (`:4187-4200`) does a **non-atomic** read-modify-write (plain `write_text`). It is also the ETA calibration source, which contention would inflate.
- Every git op on the shared ree-v3 / REE_assembly checkouts: `git_pull` `:1946`, `_pull_ree_v3` `:2271`, the stash in `_git_push_with_retry` `:2943-2946`, and the per-run `_background_sync` thread `:4652-4671`. N of these would contend for `.git/index.lock`.
- **Already safe (keyed per queue_id or pid):** sentinel `_runner_signals/<queue_id>.json` (`:4286-4297`), partial checkpoint `:4859`, and synthetic run_id `:2712`. The four on-disk tensor caches (`~/.ree_ofc_head_cache`, `~/.ree_probe_warmup_cache`, `~/.ree_maturation_prefix_cache`, `trace_store`) all write `*.tmp.{pid}` then `os.replace`, so a concurrent mint of the same key wastes compute but corrupts nothing. Arm-reuse is read-only (`experiments/_lib/arm_reuse.py:78-81`).
- `make_run_id` (`experiments/_lib/run_id.py:79`) has one-second resolution. It collides only if two slots start the **same** experiment_type in the same second, which is unlikely but not impossible for split A1 seed items (sec 2.8).

### 1.2 Coordinator (`ree-v3/coordinator/`)

- **There is no claims table.** A claim is `experiments.claimed_by_machine/claimed_at/status` (`schema.sql:10-23`), keyed by queue_id: one owner per item, unbounded items per owner.
- **`heartbeats` is one row per machine** (`schema.sql:50`, `:68` `machine TEXT PRIMARY KEY`) with a single `state`, `current_exq`, `progress_json`, `seconds_remaining`, the shutdown columns (`:76-80`) and `claim_fence_cleared_at`.
- `heartbeat_log` (`schema.sql:129-136`) appends only on a (state, current_exq) transition (`db.py:4059-4066`). Two slots alternating would append nearly every tick.
- **`_has_fresh_owner_heartbeat` (`db.py:3404-3418`)** does `SELECT ... FROM heartbeats WHERE machine=?` and then `if row["current_exq"] != queue_id: return False`.
  - **This is the load-bearing hazard.** With two slots on one name, `current_exq` belongs to whichever slot posted last, and posts come every `STATUS_WRITE_INTERVAL=5` s (`experiment_runner.py:121`).
  - Once a claim is older than `COORDINATOR_STALE_HOURS` (6, `app.py:111`), its protection flickers, and **another machine can claim an item that is still running. That is a duplicate run**, the V3-EXQ-861f pattern described at `db.py:3363-3400`.
  - A1 items are estimated at ~18-71 h per item (A1 doc sec 3), so every A1 item would cross the 6h floor.
  - **The fix is NOT lowering the 6h floor** (CLAUDE.md; memory `feedback_heartbeat_stale_not_abandoned`). It is making liveness per item (sec 4, Option C).
- `_claim_recoverable` (`db.py:3421-3445`): route (b) departure (`:3440`) OR route (a) time plus no fresh owner heartbeat. It has no caller-is-not-owner check, so on a shared name slot B could re-claim slot A's stale item on the same box.
- Claim fence `claim_fence_active` / `machine_claim_fenced` (`db.py:3493-3549`, lookup `WHERE machine=?` at `:3542-3543`), `CLAIM_FENCE_DEFAULT_SECONDS=1800`. Departure reaper `machine_departed` / `machine_has_departed` / `claim_orphaned_by_departure` (`:3637-3728`), `CLAIM_REAP_QUIET_DEFAULT_SECONDS=900`, `PROCESS_EXIT_SHUTDOWN_REASONS` (`:3480-3483`). **All of these are keyed by machine name.**
- `release_claim` (`db.py:3833-3869`) is owner-guarded by exact `claimed_by_machine`.
- `app.py` endpoints:
  - `/heartbeat` (`:1377-1402`) is an `ON CONFLICT(machine)` upsert where the last writer wins.
  - `/status` (`:1404-1426`) stores one payload per machine.
  - `/shutdown_notify` (`:1428-1472`) says in its own comment (`:1455-1458`) that "a drifted spelling here arms a fence nobody checks".
  - `/commands` (`:901-915`, `:1506-1585`) is per machine. Only `kick`/`release_claim` carry a `queue_id`, and the first ack wins.
  - `/result` (`:1587-1640`) stores the **raw** `manifest.machine` uncanonicalised in `results.machine`.
  - `/shadow/status` (`:959-1054`) returns one row per `heartbeats` row.
  - `body.machine` overrides the token label with no cross-check (`:207-217`), so a new identity string needs no new token.
- `deploy/live-status-writer.py`: `merge_alias_rows` (`:133-169`) keeps one row per canonical machine, and **the losing rows are hidden**. `build_markdown` (`:238-310`) shows one Experiment/Progress/ETA cell per machine and counts "running" as rows with `current_exq` (`:265-266`).
- `phase3_preflight.py`:
  - `orphaned_claims` (`:650-679`, SQL at `:663`) flags any claimed item whose owner row's `current_exq != queue_id`. **It fails deterministically with 2 claims on one machine.**
  - `fleet_lifecycle` (`:386-444`) expects canonical peers DLAPTOP and ree-cloud-2/3/4 (`:106-111`).
- `sync_daemon.py:914-942` reads a single `current.queue_id` per machine. That path is dormant (`PHASE3_HEARTBEAT_GIT_MATERIALIZE=0`, and it stays retired per "Closed on measurement" item 7). `_materialise_queue_from_db` (`:2449-2500`) writes `claimed_by` per item, which is fine. **`sync_daemon` stays the sole git writer under every option below.** Slots POST `/result` exactly as today.

### 1.3 Cloud scaler (`coordinator/deploy/cloud-scaler.py`, hub timer every 5 min; GHA backstop `.github/workflows/cloud-scaler.yml`, 6-hourly)

- Worker list `WORKERS` (`:235-240`) pairs hcloud name with affinity, e.g. `("ree-worker-3","ree-cloud-3",...)`. **The claim/affinity key is `ree-cloud-N`, not `ree-worker-N`.**
- **Layer 1, HUB_NAME skip** (`:132`, loop `:1091-1094`): unaffected by slots.
- **Layer 2, HELD_BY_SELF** `count_held_by_self` (`:376-396`) counts `status=="claimed"` items where `claimed_by.machine == affinity` using **exact string `==`** (`:394`); the veto is at `:1196-1203`. It counts **per claim**, so 2 claims under the plain name are correctly protected. **A slot-suffixed name is invisible to it (count 0).** The GHA duplicate is `cloud-scaler.yml:283-298` (`:295`) with veto at `:502-508`. The surge pre-check reads `worker_held["ree-cloud-2"/"-3"]` (`:1168-1174`).
- Idle gate `evaluate_heartbeat` (`:470-538`): `coord_status.get(affinity)` (`:1113`) is an exact lookup. On a miss it falls back to the retired git file, which gives `idle_ok=1 no_heartbeat` (`:502-503`). Then `state != "idle" or current_exq` means not idle (`:531-532`). `HEARTBEAT_FRESH_MIN` is at least 35 (`:125`, `:1337-1345`).
  - **With a shared name:** an idle slot's `idle / current_exq=None` post can read as `clean_idle` while its sibling runs. HELD_BY_SELF still vetoes, so this is protected by exactly one layer instead of two.
  - **With a suffixed name:** idle gives `no_heartbeat`, HELD_BY_SELF gives 0, and **the box is shut down mid-run.**
- Grace window `_last_completed_from_db` (`:449-467`) does `WHERE machine = ?` against the **raw** `results.machine`, an exact match. It is lost for suffixed names.
- Power-off `:1269-1280`: `announce_shutdown(affinity)` posts only under the base name, so fence and reaper arm for `heartbeats['ree-cloud-3']` only. `coordinator_announce_shutdown.sh:72-74` and `coordinator_clear_claim_fence.sh:61-65` reject any character outside `[A-Za-z0-9._-]`, **so a `#` suffix is refused outright.**
- Layer 3, the runner-side transient exit codes: already covered in 1.1.
- **Precedent for a second identity row per box:** `coord_status.get("%s-metaworker" % affinity)` (`:649-684`). The orchestrator heartbeats as `ree-cloud-4-metaworker`, which is its own `heartbeats` row that canonicalisation passes through unchanged.

### 1.4 Machine identity and other consumers

- `machine_identity.py`: `canonical_machine_name` (`:162-191`) collapses only `SUFFIX_BLIND_BASES={"dlaptop": ...}` (`:134-140`), and `_split_suffix` strips only a trailing `-<digits>` (`:148-159`). **`ree-cloud-3#1` and `ree-cloud-3.s1` both pass through unchanged, so `same_machine("ree-cloud-3", "ree-cloud-3.s1")` is False.** A suffixed slot could then never claim an item pinned to its own box. The resolver is an allowlist by design (CLAUDE.md machine-identity note: the `ree-cloud-N` digit IS the identity, never collapse it). **Any slot suffix therefore needs a new, separate "base machine" function, not a loosening of canonicalisation.**
- Manifest provenance: `experiments/_lib/manifest_core.py` `ALWAYS_CORE_KEYS` (`:214-223`) and `MANDATORY_CORE_KEYS` (`:261-266`) include `machine` (raw `socket.gethostname()`, `:1421`), `machine_class` (`:1423`) and `elapsed_seconds` (wall, `:1426+`). There is **no thread count and no concurrency marker.**
- `deploy/fleet_integrity_check.py` `ALLOWED_MACHINES` (`:72-76`) ALERTs on unknown names. `deploy/phase3_wake_fleet.sh:154` does an exact name match.
- **Umbrella-side consumers of "one `ree-runner` per box" (not in the brief's list; found in passing):**
  - `scripts/metaworker_role_verdict.py:66-92` `holds_claim` (exact `claimed_by.machine == machine`).
  - `scripts/ree_runner_failsafe.py` (`systemctl is-active ree-runner`, `:160-161`).
  - `ree-v3/coordinator/deploy/ree-role-arbiter.*` (dual-role ree-cloud-4 stops/starts `ree-runner`).
  - `scripts/remote_pytest.sh` (`systemctl stop/start ree-runner` `:1341`/`:1360`, plus the experiment detector `scripts/remote_pytest_detect.py --mode=experiment`).
  - All of these address the single unit name `ree-runner`, so N systemd units would escape every one of them.

### 1.5 Queue schema

- `validate_queue.py:558-588` `ITEM_REQUIRED`/`ITEM_OPTIONAL` has no `exclusive`, `slots`, `threads` or `memory_gb` field. **Unknown keys pass validation** (the loops at `:1559-1577` only type-check present fields), so an opt-out flag could be added without a schema break, but it should be registered in `ITEM_OPTIONAL` so it is type-checked.
- `estimated_minutes` is only checked `> 0` (`:1612-1617`) and is used only for ETA (`experiment_runner.py:4204`, `:4392-4435`). **The runner enforces no wall-clock timeout** (the `Popen` at `:4560-4567` has none).

## 2. Hazards and mitigations

| # | hazard | severity | mitigation (design, not built) |
|---|---|---|---|
| H1 | **Per-item liveness is per-machine.** With 2 slots on one name, `_has_fresh_owner_heartbeat` flickers, and after 6h a running item becomes claimable elsewhere, causing a **duplicate run**. | **critical; blocks any multi-slot rollout** | Per-item **lease** (`leases(queue_id PK, machine, slot, renewed_at)`) renewed by each running slot. The fresh-owner predicate becomes "lease for this queue_id renewed within X". **The 6h `COORDINATOR_STALE_HOURS` floor is untouched**; the lease only replaces how "owner is heartbeating against this queue_id" is answered. `orphaned_claims` in preflight moves to the same predicate. |
| H2 | **Scaler kills a box with a live slot.** Suffixed identities evade HELD_BY_SELF, the idle gate and the grace window. Shared identities weaken the idle gate to one layer. | **critical** | Keep the **claim owner = the plain affinity** (`ree-cloud-3`) under every option, which keeps HELD_BY_SELF correct with zero scaler change. Add a **4th layer**: "any fresh lease for this affinity" means never shut down, with identical logic in `cloud-scaler.py` and `cloud-scaler.yml` (the existing transport-parity test pins them together). The runner must report an **aggregate** machine heartbeat (`state=running` if any slot is busy), never a per-slot idle. |
| H3 | **CPU / torch-thread oversubscription.** N children each default to all cores, so K x 8 threads on 8 vCPUs thrash. | high | The runner sets per-slot `OMP_NUM_THREADS` / `MKL_NUM_THREADS` / `OPENBLAS_NUM_THREADS` (= `floor(nproc / slots)`) in `_build_subprocess_env`. Env is the only place that takes effect before `import torch` in the child. Scripts that call `torch.set_num_threads` themselves (1021, 1108) still override, so **record the truth, not the intent**: add `torch_num_threads = torch.get_num_threads()` and `torch_num_interop_threads` to `manifest_core` `ALWAYS_CORE_KEYS`, read at manifest-write time. |
| H4 | **Reproducibility across thread counts and machine classes.** BLAS reduction order depends on thread count, giving ULP-level differences. The memory note `reference-cross-machine-class-contract-divergence` measured the pipeline stable to 1e-4 perturbation, with action flips driven by `torch.multinomial` / RNG stream, not float noise. But over hours of training, ULP differences in weights are not guaranteed to stay ULP. | medium (**and already present today**, P4) | **Decision for the user:** (a) pin threads per slot and record them (recommended; required anyway for H3); (b) whether `torch_num_threads` joins the arm-reuse compatibility key. Recommended **no** for now: `machine_class` already mixes 2-thread and 8-thread runs, and adding it would fragment `arm_fingerprint_index.json` retroactively. Instead record it, and let governance treat a thread-count mismatch as an annotated, not disqualifying, difference until measured (M2 in sec 3). Contracts already assert upstream of the discrete quantizer (CLAUDE.md), so no contract change is needed. |
| H5 | **Memory / OOM blast radius.** 4 GB cpx22/cx23 boxes already OOM with ONE process (cloud-1 SD-049/050 note; the `137` comment at `experiment_runner.py:5717-5734`). With slots, the kernel OOM killer picks the largest process, which may be a **sibling**. Exit 137 is "transient", so the sibling's claim is released and re-queued, and a heavy item can repeatedly kill neighbours in a loop. | high | (1) Slots only on boxes with at least 16 GB (cx43/cx53); cpx22/cx23 stay `slots=1`. (2) Run each child in its own cgroup, `systemd-run --scope -p MemoryMax=<total/slots> -p MemorySwapMax=0` (or a `ree-runner-slot@.scope`), so an OOM kills only the offending slot. (3) Admission guard mirroring the pytest short lane (`docs/reference/ree-v3-test-suite-routing.md:39-52`): do not start slot k unless `MemAvailable` is at least the per-slot budget. (4) Optional `memory_gb` hint on the queue item; admission refuses a co-tenant slot when the sum exceeds the budget. (5) An item that OOMs **twice** under co-tenancy gets auto-marked `exclusive` rather than looping. |
| H6 | **Timing-sensitive experiments.** No PASS criterion reads wall time: every "latency" criterion counts steps or episodes (e.g. `v3_exq_250...py:103`, `v3_exq_231a...py:556`). But wall time IS recorded (`elapsed_seconds`, `v3_exq_1108...py:693/1032` `wall_s`, `v3_exq_1105b...py:352/372/849` `arm_wall_s`) and IS the calibration input (`script_timing.json`, onboarding smoke steps/s, `v3_scale_benchmark.py:137-141`, `v3_exq_070...py:189`). | medium | Queue flag `exclusive: true`: the runner admits the item only when all other slots are empty, and admits nothing else until it finishes. Default it on for the `v3_onboard_smoke_*`, `v3_scale_benchmark` and `*_calibration` families. Stamp `slot_occupancy` (max concurrent items seen during the run) and `slots_configured` into the manifest so every wall-time consumer can filter. `save_script_timing` should skip (or tag) co-tenant runs so ETAs do not inflate, and should be made atomic (tmp + `os.replace`). |
| H7 | **Git / manifest writers.** N git actors on one checkout contend for `index.lock`. The legacy git-mode claim lets the same name double-claim (`:3630-3632`). | high if N processes, low if one runner | **`sync_daemon` stays the sole coordination-data writer**; slots POST `/result` as today. Only one git actor per box: one runner process (Option B/C) does pulls. Require `COORDINATION_MODE=coordinator` for `slots>1`, **failing closed to `slots=1`** if it falls back to git mode (the git mutex cannot arbitrate same-name slots). |
| H8 | **Substrate updates vs. overlapping slots.** Pulls and self-restart need "nothing running", which never happens with staggered slots. `_substrate_freeze_blocked` would defer pulls forever. | high (a fleet running stale code indefinitely is a silent failure) | Two choices, a decision for the build session: (a) **drain window**: when a pull, parity-gate change or self-restart is pending, stop admitting new items and pull when all slots are empty. Cost: up to one item-wall (hours) of idle slots per update. (b) **Per-item immutable checkout**: each claim runs from `git worktree add --detach <sha>` of ree-v3, removed afterwards. The runner can then pull freely, and the manifest's `substrate_commit` is exact. `experiments/pack_writer.py:221-259` is already worktree-aware for the REE_assembly path, but every other `parents[N]`-relative path in `experiments/_lib` (e.g. `arm_reuse._DEFAULT_INDEX :78-81`) needs auditing first, which is a cheap check. Recommend (a) for the first box and (b) as the follow-up if the measured drain cost bites. |
| H9 | **Stale-claim recovery per slot.** With a shared name, `_claim_recoverable` lets a same-box sibling take a stale item. With suffixed names, the fence and the departure reaper never arm, because `announce_shutdown` posts under the base name only. | high | The per-item lease (H1) fixes route (a) per item. For route (b), keep claims owned by the base affinity so the existing fence and reaper keep working unchanged. **Do not lower 6h, and do not add a new absence-based route.** |
| H10 | **Remote-control commands are machine-addressed.** `force_stop` would kill `current_proc[0]`, an arbitrary slot. | medium | `force_stop`, `suspend` and `resume_run` gain an optional `args.queue_id` (as `kick`/`release_claim` already have). Without it, they apply to **all** slots. `stop`/`pause` stay machine-wide (drain or pause admission). Commands stay fetched by one process per box, so there is no double execution. |
| H11 | **Observability collapses.** `live-status-writer` hides alias rows, `/shadow/status` has one `current_exq`, `check_shadow.py` prints one `exq`. | low (but operators will misread the fleet) | The heartbeat payload gains `slots: [{slot, queue_id, progress, seconds_remaining}]`, keeping `current_exq` = the oldest running item for back-compat. The live-status table renders one sub-row per slot, and "running" counts items, not machines. |
| H12 | **Laptop yield.** A cloud box with a free slot reads as unavailable (`:3450-3452`). | low | `_cloud_worker_is_available` checks `free_slots > 0` from the new payload, falling back to today's rule when the field is absent. The Mac stays `slots=1` (its runner is user-managed and deliberately often off; memory `feedback_mac_runner_deliberately_off`). |
| H13 | **Umbrella tooling assumes one `ree-runner` unit** (failsafe, role arbiter, remote_pytest stop/start and detector). | high for Option A only | Options B/C keep exactly one `ree-runner.service` per box, so none of these change. The experiment detector already sees N `experiment` processes as "busy", which is correct. |

## 3. The measurement that decides whether to build at all (specified, NOT run)

**The unmeasured premise:** on a cx43 (8 shared vCPU), is aggregate throughput higher with K items at 8/K threads than with 1 item at 8 threads (which is what the fleet does today, P2)? If torch's intra-op scaling on A1's op shapes is near-linear to 8 threads, slots buy nothing. If it saturates at ~2 threads, which is plausible for small MLP batches, slots are worth up to ~4x.

**M1 -- thread scaling, one item (`S(T)`).**
- Workload W: a fixed, seeded, bounded slice of the A1 GROUNDED arm (the paired-agent probe harness behind `a1_cost_remeasure_20260926.md` sec 8, which already exists as a probe), sized to ~10 min at 2 threads.
- For T in {1, 2, 4, 8}: set `OMP_NUM_THREADS=MKL_NUM_THREADS=T` in env plus `torch.set_num_threads(T)`, `set_num_interop_threads(1)`.
- 3 repeats per T, **interleaved order** (the cx line is shared-vCPU: noisy neighbours and CPU credits; see `ree-v3-test-suite-routing.md`, where an 8-vCPU box ran a single-threaded suite ~1.8x slower than a 2-vCPU box).
- Record wall, `torch.get_num_threads()`, load1, and peak RSS (`/usr/bin/time -v`).

**M2 -- concurrency at fixed cores (the decisive one).**
- Same W, K concurrent copies at T=8/K: (K,T) in {(1,8), (2,4), (4,2), (8,1)}, 3 interleaved repeats.
- Throughput = K / wall_of_the_batch (items per hour). Also record per-copy peak RSS (it sizes H5), and whether outputs at different T are bit-identical at the same seed. Hash final weights and the action stream at `%.17g` (this sizes H4).

**Decision rule, to be pre-registered before running:**
- `best_K>1 throughput / (K=1,T=8) throughput >= 1.5`: multi-slot is worth building.
- `< 1.2`: do not build. Instead pin threads (policy only) and scale horizontally (Option 0).
- Between those: user call, weighed against build cost.

**Where to run it (user OK needed either way):**
- (i) A **throwaway cx43** provisioned for ~2 h. Roughly EUR 0.06 at EUR 0.0315/h (A1 doc sec 4), plus venv setup matching the hub's pinned `pip freeze` (P7 precedent). It **never touches the live fleet**, but it is provisioning, which the user has not authorised.
- (ii) `ree-worker-3` / `ree-cloud-3` while idle, stopping its runner the way `remote_pytest.sh` does (`:1341`/`:1360`). It uses a live worker and competes with the queue.
- Recommended: (i).
- ~2 h wall, not measured on the Mac (different machine class and thread behaviour).

## 4. Design options

There are two independent axes: **runner topology** (N processes vs. one process with a pool) and **liveness protocol** (per-machine heartbeat row vs. per-item lease). H1/H2/H9 show that the protocol axis is mandatory: without per-item liveness, no multi-slot design is safe past 6 h.

### Option 0 -- Do not build slots; pin threads and add boxes (the comparator)
- **What:**
  - Set a per-box thread policy (env in `shadow.conf`) and record `torch_num_threads` in manifests. That is worth doing regardless (P4).
  - Get concurrency from more workers: add `ree-cloud-5+`-style runner boxes (cx43 at EUR 0.0039/core-h is already the cheapest per core).
- **Touches:**
  - scaler `WORKERS` and the GHA list
  - `LAPTOP_YIELD_CLOUD_HOSTS` (`:3372-3377`)
  - `fleet_integrity_check.ALLOWED_MACHINES` (`:72-76`)
  - `phase3_preflight.EXPECTED_LIFECYCLE_PEERS` (`:106-111`)
  - provisioning plus venv parity per box
  - **zero runner/coordinator protocol change**
- **Cost:** EUR is trivial either way (A1 doc sec 5: every option is under ~EUR 300 per campaign). The real cost is per-box operational surface: venv drift, git-wedge exposure, and scaler list edits.
- **Unmeasured premise:** Hetzner project server quota. Check `hcloud` limits before assuming N more boxes.
- **Choose if:** M2 < 1.2x, or if calendar time matters more than engineering time.

### Option A -- N runner processes per box, each a pseudo-machine (slot suffix)
- **What:**
  - `ree-runner@1..N.service`, each `--machine ree-cloud-3.s<k>`. A `#` suffix is ruled out, because `coordinator_announce_shutdown.sh:72-74` rejects it; `.` passes.
  - Each process has its own heartbeat row, so `_has_fresh_owner_heartbeat` works per slot unmodified. That is the attraction.
- **Breaks, silently, unless every consumer is taught a new `base_machine()`:**
  - scaler HELD_BY_SELF (`:394`, GHA `:295`)
  - idle-gate lookup (`:1113`)
  - grace window (`:449-467`)
  - `announce_shutdown` / fence / reaper (they arm the base row, and the slot rows are never fenced)
  - affinity (`same_machine` never matches the base)
  - `fleet_integrity`, `phase3_wake_fleet.sh`, live-status, `metaworker_role_verdict.holds_claim`
  - every `ree-runner` unit consumer (failsafe, arbiter, remote_pytest)
- **Also:** N git actors on one checkout, `runner.pid` and `script_timing.json` / `experiment_queue.json.tmp` races (H7), and N command pollers.
- **Verdict:** lowest runner change, highest **silent-failure surface**. Each missed consumer fails *open* (the scaler kills a live box, or a fence nobody checks), which is exactly the class `app.py:1455-1458` warns about. **Not recommended.**

### Option B -- One runner per box with an internal slot pool; per-item liveness in the heartbeat payload
- **What:**
  - The runner becomes a dispatcher: an admission loop plus one pump thread per slot (each pump owns its child, progress closure and per-slot flags).
  - All claims are owned by the plain affinity, so HELD_BY_SELF, fence, reaper, affinity and every `ree-runner` consumer stay **correct unchanged**.
  - The heartbeat payload carries `slots: [...]`. The coordinator stores it and `_has_fresh_owner_heartbeat` checks **membership** (`queue_id in running_set`) instead of equality.
  - One git actor, one pid, one command poller.
- **Runner changes:**
  - `_current_claim` / `_current_proc` / flags become per-slot maps
  - signal handling and `_do_immediate_exit` release all held claims
  - drain waits for all slots
  - self-restart and pulls use a drain window (H8a)
  - commands gain optional `queue_id` targeting (H10)
  - admission implements thread env (H3), cgroup memory caps and `MemAvailable` (H5), `exclusive` (H6), and coordinator-mode-only (H7)
- **Coordinator changes:**
  - store the slot set (new column or small table)
  - membership predicate in `_has_fresh_owner_heartbeat` and preflight `orphaned_claims`
  - aggregate `state`
  - live-status sub-rows
  - `/shadow/status` field
- **Verdict:** the largest runner refactor (the main loop is currently synchronous with the stdout pump on the main thread), but the fewest silent-failure edges. Liveness is still coupled to one per-machine row, so one post carries all N items, and a runner-thread wedge on one slot is invisible to the others' liveness.

### Option C -- Coordinator-side per-item slot leases, plus capacity; pooled runner topology (B's runner)
- **What:** B's runner, but liveness becomes an explicit protocol instead of a heartbeat payload:
  - `leases(queue_id PK, machine, slot, granted_at, renewed_at)`. Each slot's pump renews its own lease (`POST /lease/renew {queue_id, machine}`) on the existing 5 s cadence.
  - `_has_fresh_owner_heartbeat` becomes `_has_fresh_lease(queue_id)`.
  - The machine heartbeat row stays per machine and means only *machine* liveness (its current meaning for the fence, reaper and `lifecycle_state`).
  - **Capacity is server-enforced:** `machines.slots` (config, default 1), and `try_claim` refuses when `count(claimed by machine) >= slots`. The cap then survives a runner bug, restart or misconfiguration, and the coordinator (not N runner processes) is the single arbiter.
  - Scaler 4th layer = "fresh lease for affinity" (H2).
  - `exclusive` is enforced server-side too: an exclusive item is claimable only when the machine holds 0 claims, and nothing else is claimable while it runs.
- **Why over B:**
  - **The lease is shadowable** (sec 5 Phase 1): at `slots=1` a lease predicate can run beside the current heartbeat predicate with a divergence counter, and no authority, before anything depends on it. That is the shadow-first pattern the user chose for the coordinator itself (memory `feedback_infra_shadow_first`).
  - Per-item renewal means a wedged slot pump stops renewing **its own** lease only.
  - Server-side capacity makes "N" a coordinator config value, adjustable without redeploying runners.
- **Cost:** B's runner refactor, plus one table, 1-2 endpoints and one predicate swap in the coordinator. The coordinator part is the smaller half.

## 5. Rollout (if Option C, or B, is chosen)

Each phase has a go/no-go, and **nothing advances without the user confirming the previous phase proved out.**

| phase | what | where | gate to advance |
|---|---|---|---|
| **P0** | M1/M2 (sec 3) with a pre-registered decision rule | throwaway cx43 (user OK) | M2 ratio >= 1.5 (or user call in 1.2-1.5). **Below 1.2, stop here and take Option 0.** |
| **P1** (bit-identical at slots=1) | (a) Manifest records `torch_num_threads`, `torch_num_interop_threads`, `slot_occupancy`, `slots_configured` (record-only; no pinning yet). (b) Coordinator `leases` table plus runner lease renewal, env-gated, running **in shadow**: `_has_fresh_owner_heartbeat` stays authoritative, the lease predicate is computed beside it, and divergences are counted in `/shadow/status`. (c) Make `save_script_timing` atomic, and fix the `--dry-run` `runner.pid` unlink (both are independent of slots). | `ree-v3` `integration/runner-multislot` (executable-code plane, multi-session, **would break the fleet if half-landed**, so the CLAUDE.md Git Policy exception applies). Merge gated on the full contract suite via `remote_pytest.sh` plus `coordinator/phase3_preflight.py`. | >= 7 days fleet-wide with **0 predicate divergences** and 0 new orphaned-claim findings |
| **P2** | Flip the lease predicate authoritative, still `slots=1` everywhere. Scaler 4th layer (lease veto) in `cloud-scaler.py` and `.yml`, with the parity test extended. Preflight `orphaned_claims` moves to leases. | same branch, landed to `main` | >= 7 days: 0 duplicate runs, 0 scaler kills of a box with a fresh lease, fence/reaper counts unchanged vs. baseline |
| **P3** | Pooled runner (`REE_RUNNER_SLOTS`, default 1, which must keep single-slot behaviour **bit-identical**, pinned by a contract test on the heartbeat/status payload shape). Per-slot thread env, cgroup memory cap, `MemAvailable` admission, `exclusive`, coordinator-mode-only fail-closed, command `queue_id` targeting, live-status sub-rows, laptop-yield `free_slots`. Server-side `machines.slots` cap. | integration branch; full suite plus preflight gate | contract suite green on a worker; preflight green |
| **P4** | **One box**, `ree-cloud-3` (cx43, 16 GB), `slots=2`, set via coordinator config. Everything else stays `slots=1`. | ree-cloud-3 only | 7 days or >= 10 items: 0 duplicates, 0 OOM kills of a sibling, 0 lease-live scaler kills, throughput within 20% of M2's prediction, manifests from co-tenant runs pass `validate_recording` |
| **P5** | Widen: `slots=3-4` on cx43, or a cx53 (16 vCPU/32 GB) as the A1 box at `slots` sized by M2's per-copy RSS | user decision | -- |

Test files that currently pin one-item-per-machine behaviour, and will need extending (never weakening):
- `coordinator/`: `test_stale_claim_reaper.py`, `test_shutdown_notify.py`, `test_heartbeat_log.py`, `test_machine_identity_ingest.py`, `test_phase3_preflight.py`, `test_shadow_e2e.py`, `test_phase3_claim_guard.py`, `test_cloud_scaler_*` (4 files), `test_phase3_command_channel.py`, `deploy/test_live_status_writer.py`.
- `tests/contracts/`: `test_laptop_yield_busy_cloud.py`, `test_runner_heartbeat_write_gate_preserves_coordinator_post.py`, `test_machine_identity.py`.
- Umbrella: `scripts/test_ree_runner_failsafe.py`, `scripts/test_hygiene_tick_role_arbitration.py` (unchanged under B/C; they must stay green).

## 6. Recommendation (for the user; nothing decided)

1. **Measure first (P0).** It is the cheapest step (~2 h, ~EUR 0.06 on a throwaway cx43) and the only one that can say "don't build". The whole case for slots rests on torch intra-op scaling saturating below 8 threads on A1's shapes, which nobody has measured (A1 doc sec 6).
2. **Independent of slots, do the record-only half of P1(a) now:** stamp `torch_num_threads` in manifests. Thread count is already an unrecorded variable across the fleet (P4), and this costs nothing.
3. **If M2 clears the bar: Option C** (per-item leases with server-side capacity) on B's pooled runner, rolled out P1 -> P5, shadow-first.
4. **If M2 does not clear the bar: Option 0.** Pin threads per box and add boxes. Check the Hetzner server quota first.
5. **Option A is not recommended.** It looks cheapest, but every missed `base_machine()` consumer fails open. The worst case is the scaler powering off a box mid-run, and there are at least 10 such consumers across two repos.

**Decisions the user owns** (none taken here):
- (D1) authorise P0 and where it runs (throwaway box vs. idle ree-cloud-3);
- (D2) the decision-rule thresholds (1.5 / 1.2);
- (D3) whether `torch_num_threads` joins the arm-reuse compatibility key (recommended: record, do not key);
- (D4) drain-window vs. per-item checkout for H8;
- (D5) Option 0 vs. C after P0.

## 7. Closed-on-measurement items respected

- The hub runner stays retired (item 8). Slots are proposed for workers only, never `ree-cloud-1`.
- There is no hub heartbeat git writer (item 7). Slot telemetry is coordinator-only, like all telemetry.
- `COORDINATOR_STALE_HOURS` stays 6. The lease replaces *how* owner liveness is read, not the floor.
- No ref-move or pre-push guard is proposed for hub or workers (items 1-2).

## 8. Found in passing (not slot work; flagged, not fixed)

- `experiment_runner.py:5166` + `:5356`: `--dry-run` overwrites and then unlinks a **live** runner's `runner.pid` (read by `REE_assembly/serve.py:228`).
- `experiment_runner.py:4187-4200`: `save_script_timing` is a non-atomic read-modify-write.
- `experiment_runner.py:4981-4987`: the `--machine any` help text promises affinity-filter bypass that `_affinity_matches` does not implement.
