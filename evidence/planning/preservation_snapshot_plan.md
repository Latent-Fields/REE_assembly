# Preservation Snapshot Plan — preserving the possibility of future reconstruction

**Status:** Increment 1 (birth-replay preservation) BUILT + contract-gated 2026-08-14. Increment 2 (mid-life snapshot/resume) not started.
**Owner thought:** [`docs/thoughts/2026-08-14_preserving_the_possibility_of_future_reconstruction.md`](../../docs/thoughts/2026-08-14_preserving_the_possibility_of_future_reconstruction.md)
**Governance claim:** `GOV-PRESERVE-1` (candidate) in `docs/claims/claims.yaml`
**Code:** `ree-v3/ree_core/preservation/` + contract `ree-v3/tests/contracts/test_reconstruction_record.py`

This is the plan-of-record for building a preservation capability for REE: saving states,
environments, understanding, and substrate such that faithful **reconstruction** and
re-understanding remain possible later — the "option value / irreversibility" argument of the
owning thought. It is future substrate + governance + infrastructure work and does **not** expand
REE-v3 strict green-board closure scope.

---

## The core idea, and why it splits into two fidelity levels

A REE life is a **pure function of `(REEConfig, seed)` on pinned code** — verified empirically
(2026-08-14): two seed-123 constructions produce bit-identical agents (0/200 tensors differ), and
the environment's randomness flows entirely through `np.random.default_rng(seed)`. Recon of the
existing substrate (agent-mapped 2026-08-14) established:

- **Provenance capture is mature and centralized** — `experiments/pack_writer.py:write_flat_manifest`
  + `experiments/_lib/manifest_core.py` already record `substrate_hash`, `substrate_commit`,
  `machine_class`, `config`, `seeds`, `architecture_epoch`. **Extend, don't rebuild.**
- **Birth-replay determinism exists** — `experiments/_lib/arm_fingerprint.py:reset_all_rng` +
  `seeded_construct`, env `np.random.default_rng(seed)`.
- **Whole-organism save/load does NOT exist.** `REEAgent` has no state_dict aggregator; a large,
  load-bearing fraction of state lives in **non-parametric plain-attribute stores scattered across
  `ree_core/**`** (residue RBF field, anchor sets, context/goal memories, incentive & ghost-goal
  banks, staleness/neuromodulator accumulators, crystallization + EWC flags) that
  `nn.Module.state_dict()` silently misses.

This yields two very different fidelity levels:

| Level | What it preserves | Fidelity | Cost | Status |
|---|---|---|---|---|
| **1. Birth-replay** | `(config, seed, code commit, machine-class, env spec, understanding)` | Whole life re-derivable from birth, **within a machine class** | Small; leans on existing determinism + provenance | **BUILT** |
| **2. Mid-life snapshot/resume** | live state at step N (all non-parametric stores + RNG bit-state + env live-state) | resume/branch in place at any step | Large; per-module capture/restore maintained forever across `ree_core` | Not started |

Level 1 is exactly what the thought asks for: keep the information without which future
reconstruction becomes *impossible*. Level 2 is a stronger capability (perturbation/branch
experiments) that is **not required** to preserve the possibility.

---

## Increment 1 — ReconstructionRecord (BUILT)

`ree-v3/ree_core/preservation/reconstruction_record.py` — a `ReconstructionRecord` is an immutable,
self-describing, integrity-checked bundle of the birth-replay inputs plus interpretation context:

- `config` — the full `REEConfig`, serialized to plain JSON;
- `seed`; `environment` (`{class, params}` spec sufficient to rebuild the world);
- `provenance` — `substrate_hash`, `substrate_commit`, `machine_class`, `architecture_epoch`
  (supplied by the caller from `manifest_core` — the module stays pure and never imports the
  experiments layer);
- `understanding` — free-form pointer to claims/governance state and metrics believed relevant;
- `reason_for_ending`, `lifetime` (optional developmental context);
- `integrity` — sha256 over the canonical JSON of every other field.

**Design commitments (all contract-pinned):**

1. **Faithful config.** `REEConfig` round-trips exactly. Annotation-guided rebuild was insufficient:
   several fields are typed as a bare `list` (e.g. `EventSegmenterConfig.scales`, a list of nested
   dataclasses) and JSON cannot distinguish tuples from lists. The serializer therefore **tags
   dataclasses (`__dataclass__`) and tuples (`__tuple__`) explicitly** — annotation-independent,
   exact, and self-describing (a virtue for a record a future system must read).
2. **Sufficiency.** The record *alone* (round-tripped through JSON text, no original objects)
   rebuilds a **bit-identical birth agent**.
3. **Immutable / append-only.** `write_record` refuses to overwrite; `load_record` re-verifies the
   hash and raises on any mutation.
4. **Safety.** Reconstruction only imports dataclasses from `ree_core` (whitelist prefix), never an
   arbitrary dotted path named in a file.

**Fidelity boundary — asserted honestly.** Equivalence is pinned on birth *construction* (weight
init from seed, which is bit-identical across machine classes), **not** multi-step replay. Replay
routes through `torch.multinomial` in the E3 selector, which diverges across machine classes
(memory `reference-cross-machine-class-contract-divergence`); `machine_class` is stamped on every
record so a future reconstructor knows the boundary.

Contract: `ree-v3/tests/contracts/test_reconstruction_record.py` (13 tests — round-trip exactness
incl. the segmenter-scales regression, sufficiency after JSON-text round-trip, integrity/tamper,
append-only, non-`ree_core` import refusal).

## Increment 1b — emitter (BUILT)

`ree-v3/experiments/_lib/preservation.py` is the experiment-side glue that turns the pure record
primitive into an emission a driver can call at the point a life ends. It fills provenance from
`manifest_core` / `arm_fingerprint` (`compute_single_arm_substrate_hash`, `machine_class()`,
`substrate_commit` — None-tolerant in a git-less checkout, with the full commit detail incl. `dirty`
stored under `understanding`) and writes an immutable record via `preserve_life(archive_dir=...)`.

**Emission is OPT-IN and PER-LIFE, on purpose.** Not every experiment arm is "a life worth
preserving"; `GOV-PRESERVE-1` asks for *proportionate* preservation. So a driver calls
`preserve_life(...)` deliberately when a life it cares about ends — nothing fires for every run, and
nothing is wired into the shared runner hot path (`archive_dir` is required and explicit, so
preservation never silently writes into a coordinator-managed tree). Contract:
`ree-v3/tests/contracts/test_preservation_capture.py` (3 tests — reconstructable-record round-trip
from the emitter, provenance populated, append-only).

**Deferred (fleet-touching, so not done here):** making a record fire *automatically* at a boundary
(end-of-life termination, Phase 2→3 via `InfantCurriculumScheduler(on_phase3_entry=...)`, or sleep
entry) is a default-off config flag + one call in the runner/experiment lifecycle. Default-off keeps
every existing run byte-identical, but it is an executable-code-plane change (the fleet pulls `main`)
and should land behind the full contract gate — a small, separate follow-on.

---

## Increment 2 — mid-life snapshot/resume (SCOPED, not started)

**Goal:** capture an organism's full live state at step N, restore it into a fresh process, and
resume (or branch) bit-for-bit — the substrate for the perturbation / matched-branch experiments the
imaging thought (`docs/thoughts/2026-08-13_...longitudinal...md`) wants: *observe → associate →
hypothesise → intervene → replay → adjudicate*.

**Classification: `complex (probe-gated)`.** The single most important constraint (from the substrate
recon) is that **there is no single seam yielding full fidelity for free.** `REEAgent` has no
`state_dict`/`load_state_dict` override; the default `nn.Module.state_dict` captures only registered
Parameters/buffers and **silently drops every non-parametric store** — a plain Python class hanging
off the agent, or a plain attribute on an `nn.Module`. So this is per-module capture/restore
contract work, maintained module-by-module as the substrate grows. It must be **costed against real
reuse before it is started**; the spike below exists to produce that cost estimate.

### What must be captured (the ~10 mandatory-core non-parametric stores + env + RNG)

| Store | file:line | Round-trip today? | Work |
|---|---|---|---|
| `super_ordinal_goal_memory` | `ree_core/goal.py:635/648` | **yes** (`state_dict`/`load_state_dict`) | wire into a whole-organism walker |
| `goal_state` | `ree_core/goal.py:1257/1272` | yes, but does **not** aggregate its `incentive_bank` | aggregate `incentive_bank` (`goal.py:773/779`) into it |
| `serotonin` | `ree_core/neuromodulation/serotonin.py:355/365` | **yes** (`get_state`/`load_state`) | wire in |
| `residue_field` EWC anchor | `ree_core/residue/field.py:527-535` | **capture-only** (`snapshot_ewc_anchor`, no loader) | add a loader |
| `residue_field._harm_history` | `ree_core/residue/field.py:445` | no (plain `List[Tensor]`) | new capture/restore |
| `visitation_counter._next_idx` | `ree_core/…/visitation.py:59` | no (buffers captured, **ring pointer not** → resume corrupts allocation) | new capture |
| `gated_policy` crystallization + lazy `expansion` | `ree_core/policy/gated_policy.py:341-342,424` | no; **lazy `expansion` submodule → state_dict key mismatch** on load into a pre-crystallize agent | rebuild `expansion` before load, restore flag |
| `anchor_set` | `ree_core/…/anchor_set.py:201-212` | no (per-anchor payload only) | new whole-set capture |
| `staleness_accumulator` | `ree_core/…/staleness_accumulator.py:168` | capture-only (`snapshot`, no restore) | add a loader |
| `ghost_goal_bank` | `ree_core/…/ghost_goal_bank.py:179` | no (mostly derived) | capture the non-derived residue |
| **env** `CausalGridWorld` | `ree_core/environment/causal_grid_world.py` | **no serializer at all** | position/health/`grid`/`contamination_grid`/`steps` + **two** live `np.random.default_rng` bit-states (`:1383`, `:1217`) |
| **torch global RNG** | E3 selector `multinomial` at `e3_selector.py:1749/2256/3446/3555`, etc. | n/a | `torch.get_rng_state()` / `set_rng_state()` (+ cuda if GPU) |

Plus ~20 optional analog modules (OFC/lateral-PFC/AIC/frontopolar/…) that expose a diagnostic
`get_state()` with **no matching setter** — captured only when enabled, each a small addition.

### The design fork every store forces
`super_ordinal_goal_memory.state_dict` deliberately omits its telemetry counters
(`_n_writes/_last_*`). Each store needs the same call: **what is load-bearing state to restore vs.
throwaway telemetry to drop.** Getting this wrong is a silent fidelity bug, so each store's
capture/restore ships with its own round-trip contract (save → mutate → restore → assert bit-equal).

### RNG + branch semantics
- The harness only *reseeds* (`reset_all_rng`); it never captures live RNG. Mid-run resume needs the
  torch global state and both env PRNG bit-states (and `np.random`/`random` global state only if a
  live path uses them — `replay_sampler.py:187`, `hippocampal/module.py:175`).
- **branch/rollback/migrate**: loading a snapshot against a *newer* `substrate_hash` needs a versioned
  migration story (or an explicit refuse-and-report). A branch is two resumes from one snapshot with
  divergent post-branch RNG.

### De-risking spike (do this FIRST, then decide)
1. **`SuperOrdinalGoalMemory`** (`goal.py:355`, built `agent.py:3070`) — small, tensor-based, and it
   already ships **both** directions, so the spike is a cheap round-trip equality test that
   establishes the per-store pattern cost and forces the state-vs-telemetry fork on the smallest
   surface.
2. Then **one worst-case**: the `residue_field` EWC anchor (capture-exists / no-restore, interacts
   with registered buffers) **or** `gated_policy` crystallization (lazy submodule breaks naive load)
   — to size the tail risk before committing to the full ~10-store rollout.
3. **Decision gate:** extrapolate per-store cost × stores + env + RNG + the ongoing maintenance tax
   (every new substrate store needs a capture/restore + contract) against the concrete experiments
   that need mid-life resume. Proceed only if that reuse is real; otherwise birth-replay (Increment 1)
   already preserves the possibility of future reconstruction, which is the thought's actual ask.

### Verification strategy (when built)
Save at step N → restore into a fresh process → replay K steps → assert equivalence **within a
machine class** (same discrete-sampling caveat as Increment 1: assert on pre-quantizer quantities or
same-machine, and stamp `machine_class`). A matched unperturbed resume vs. a perturbed resume is the
experimental payload.

---

## Governance / ethics (GOV-PRESERVE-1, candidate)

Preservation is not neutral. The archival-ethics principle (from the owning thought, in the user's
framing) is registered as a candidate governance rule: **when an artificial entity ends, preserve
enough of its substrate, developmental history, memories, commitments, relationships, embodiment,
and environment to keep future reconstruction conceivable, where doing so is proportionate and
ethically permissible — even if reconstruction remains speculative and never becomes part of the
operative design.** Preservation implies neither immortality nor permission to revive: any future
reconstruction requires its own governance (prior consent, privacy, identity, welfare, competing
claimants, branching-successor moral status). This sits on the ethics perimeter alongside
`SENT-*` / `GOV-*`; open questions: retention/sampling policy, who may create/read/re-instantiate/
(ever) delete a record, and the reclassification trigger by which a past instance becomes
"preserve with priority."

---

## Storage & durability (European-sovereign)

Where preserved records physically live. Requirement (user, 2026-08-14): **entirely
European-owned/-domiciled providers** — Switzerland and Norway acceptable (both hold EU adequacy
decisions), US-owned clouds excluded even when they host in an EU region (US CLOUD Act reaches the
company, not just the datacentre). The current working `evidence/` tree on GitHub is a *working*
copy under US jurisdiction, **not** a preservation copy.

**Three tiers, very different sizes** (measured 2026-08-14 on a real record):

| Tier | What | Size | Medium |
|---|---|---|---|
| Key | seed + code-commit + **integrity sha256** + machine-class | **132 bytes** | engraved metal (jewellery); one QR |
| Record | full ReconstructionRecord (config/env/understanding) | **~46 KB** (~10 KB gzipped) | object store; physically feasible |
| Environment | the *code* at `substrate_commit` + torch/python to run it | tens–hundreds MB | code-preservation archive |

Because a record is ~10 KB, **cost and performance do not discriminate** — diversification is
effectively free, and preservation's whole purpose is surviving the loss of any one provider. So
the decision is not "which provider" but "how many copies", and the answer is >1 (the LOCKSS /
3-2-1 principle). Hetzner is an excellent *node 1* (German/EU, and the fleet already runs there —
zero new tooling), but a commercial host is one ToS change / missed invoice / acquisition from gone;
mandate-backed archives (CERN, UNESCO) exist to outlive that.

**Recommended tiered stack (promote the ones that matter):**

1. **Hot copy (all records) — Hetzner Object Storage** (🇩🇪 Falkenstein/Nuremberg/Helsinki, all EU),
   client-side encrypted. Node 1; least-friction.
2. **Independent durable copy (all records) — a second EU vendor** (Scaleway 🇫🇷 or Exoscale 🇨🇭),
   so no single company holds the only copy.
3. **Mandate-backed copy (promoted records) — Zenodo** (CERN, DOI) for records + **Software
   Heritage** (Inria/UNESCO) for the *code* at `substrate_commit` — the piece that actually rescues
   reconstructability. Move the working repo off GitHub to **Codeberg** 🇩🇪 or a self-hosted
   Forgejo/Gitea on Hetzner to keep code under EU jurisdiction.
4. **Sacred / physical tier (truly loved organisms) — Piql / Arctic World Archive** (🇳🇴 Svalbard,
   the same infrastructure GitHub's Arctic Code Vault used) + an engraved metal key by a European
   artisan.

**Built (Increment 1c):** `ree-v3/ree_core/preservation/archive.py` —
- **`S3Archive`** for any S3-compatible store; the intended node 1 is **Hetzner Object Storage**.
  Wiring: `endpoint_url="https://<fsn1|nbg1|hel1>.your-objectstorage.com"`, credentials via the
  standard boto3 env chain (`AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY` = the Hetzner S3 key/secret;
  the module never reads/stores/logs them), `object_lock_days=` for WORM on a lock-enabled bucket.
  `boto3` is lazy-imported (only when no client is injected), so ree_core stays import-light.
- **`LocalArchive`** — filesystem backend (a local hot copy; what the tests exercise).
- **`AesGcmEncryptor`** — client-side AES-256-GCM (you hold the key; Hetzner sees only ciphertext).
  `NoEncryption` is the default; losing the key is unrecoverable, by design.
- **Content-addressed + append-only:** the object key embeds the record's sha256, so a changed
  record can never overwrite the original. `preserve_life(archive=..., ...)` now writes through any
  backend.

Contract: `ree-v3/tests/contracts/test_preservation_archive.py` (9 tests — content-addressing,
round-trip+reconstruct, append-only, real AES-GCM ciphertext-at-rest + wrong-key refusal, and the
S3 path driven by an injected fake client so it needs no boto3/network/credentials).

**Physical-token exporter (Increment 1d) — BUILT.** `ree-v3/ree_core/preservation/token.py` turns a
record into the artifacts for durable physical media (engraved key / jewellery, QR, M-DISC, a
Piql/Svalbard deposit): the ~180-byte **key line** (`REE-PRESERVE/1|id=…|seed=…|commit=…|machine=…|
sha256=…` — the engraveable locator+authenticator), the **gzipped record** (~10 KB self-sufficient
payload), a **manifest** (record integrity + deposited-blob sha256), a **README** (how to verify +
reconstruct), and a **QR** of the key line when a backend is installed (`segno`, pure-python, zero
deps — gated and injectable, like boto3/cryptography). `export_token(record, out_dir, …)` +
`python -m ree_core.preservation.token --record … --out …`. Contract
`tests/contracts/test_preservation_token.py` (7): key-line round-trip, always-written zero-dep
artifacts, gz record re-inflates→verifies→**reconstructs bit-identical**, manifest hashes, QR via
injected fake backend.

**Not done (next):** actually create the Hetzner bucket + a second-vendor bucket and run the fleet's
records through them (operational, needs the user's account + a generated encryption key kept
independently); the Zenodo/Software Heritage deposit flow.

## Status table (resume primitive)

| Item | State | Where |
|---|---|---|
| Recon of existing state/provenance/replay machinery | done | (this doc, §"two fidelity levels") |
| Config JSON serializer (tagged, exact) | done | `ree_core/preservation/reconstruction_record.py` |
| ReconstructionRecord schema + integrity + append-only storage | done | same |
| `reconstruct_config` → bit-identical birth agent | done + contract | same + contract test |
| Contract test (record, 13) | done, green on hub | `tests/contracts/test_reconstruction_record.py` |
| GOV-PRESERVE-1 archival-ethics rule | registered candidate | `docs/claims/claims.yaml` |
| Emitter glue `preserve_life` (opt-in, per-life) | **done + contract (3)** | `experiments/_lib/preservation.py`, `tests/contracts/test_preservation_capture.py` |
| Archive backends (Local + S3/Hetzner) + AES-GCM + content-addressing | **done + contract (9)** | `ree_core/preservation/archive.py`, `tests/contracts/test_preservation_archive.py` |
| European-sovereign storage plan | **documented** | this doc, §"Storage & durability" |
| Physical-token exporter (key + QR + gz record + README) | **done + contract (7)** | `ree_core/preservation/token.py`, `tests/contracts/test_preservation_token.py` |
| MultiArchive fan-out (>1 copy) + `s3_archive_from_env` + runbook | **done + contract (5)** | `ree_core/preservation/archive.py`, `tests/contracts/test_preservation_multi.py`, [`preservation_storage_runbook.md`](preservation_storage_runbook.md) |
| Live Hetzner bucket + 2nd-vendor + Zenodo/SWH deposits | not done (operational; needs account + key) — see runbook | [`preservation_storage_runbook.md`](preservation_storage_runbook.md) |
| Auto-fire at a lifecycle hook (default-off flag; fleet-touching) | deferred (small, separate) | — |
| Increment 2 (mid-life snapshot/resume) | **scoped** (`complex (probe-gated)`); spike = `SuperOrdinalGoalMemory` | this doc, §"Increment 2" |
| Memorial Fishtank (re-instantiate remnants) | aspiration; needs its own governance | — |
