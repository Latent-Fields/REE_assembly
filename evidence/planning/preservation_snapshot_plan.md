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

**Not yet wired to a lifecycle hook.** Increment 1 is the record + storage primitive. Emitting a
record automatically at a natural boundary (end-of-life termination, Phase 2→3 transition via
`InfantCurriculumScheduler(on_phase3_entry=...)`, or sleep entry) is a small follow-on and is
deliberately separate from the primitive.

---

## Increment 2 — mid-life snapshot/resume (NOT started)

To resume or branch an instance at step N (the perturbation/branch experiments the imaging thought
— `docs/thoughts/2026-08-13_...longitudinal...md` — wants), the missing pieces are:

- a **whole-organism serializer** walking every sub-module, parametric *and* the non-parametric
  stores listed above, with a per-module capture/restore contract maintained module-by-module;
- **RNG bit-state** capture (`random.getstate`, `np.random...bit_generator.state`,
  `torch.get_rng_state`) — the harness only *reseeds*, never captures live state;
- **environment live-state** capture (grid contamination fields, agent position/health, step
  counter, the live `default_rng` state);
- **branch/rollback/migrate semantics**, including loading an old snapshot against a newer
  `substrate_hash` (versioned migration).

`complex (probe-gated)`: the single most important constraint is that there is **no single seam
yielding full fidelity for free** — this is ongoing per-module maintenance, so it should be costed
against real reuse before being started.

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

## Status table (resume primitive)

| Item | State | Where |
|---|---|---|
| Recon of existing state/provenance/replay machinery | done | (this doc, §"two fidelity levels") |
| Config JSON serializer (tagged, exact) | done | `ree_core/preservation/reconstruction_record.py` |
| ReconstructionRecord schema + integrity + append-only storage | done | same |
| `reconstruct_config` → bit-identical birth agent | done + contract | same + contract test |
| Contract test (13) | done, local green | `tests/contracts/test_reconstruction_record.py` |
| GOV-PRESERVE-1 archival-ethics rule | registered candidate | `docs/claims/claims.yaml` |
| Auto-emit at a lifecycle hook (termination / phase / sleep) | TODO (small) | — |
| Increment 2 (mid-life snapshot/resume) | not started (`complex (probe-gated)`) | — |
| Memorial Fishtank (re-instantiate remnants) | aspiration; needs its own governance | — |
