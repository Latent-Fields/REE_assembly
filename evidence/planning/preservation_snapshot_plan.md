---
# Closure-map GOVERNANCE-lane view. Filed `generation: governance` (not v3) for
# two independent reasons:
#   (1) SCOPE -- this plan's own opening states it "does not expand REE-v3
#       strict green-board closure scope", so counting its nodes in the V3
#       closure % would inflate the V3 denominator with work V3 does not gate on.
#   (2) LANE DISCRIMINATOR -- the plan owns exactly one claim, GOV-PRESERVE-1
#       (claim_type: governance_rule, claim_level: governance, depends_on
#       SENT-0/SENT-11/SENT-12), and section "Governance / ethics" places it
#       "on the ethics perimeter alongside SENT-* / GOV-*". That is the
#       governance lane's positive test. The `process` lane was the other
#       candidate and fits the shape of what is BUILT here (archive backends,
#       emitter, token exporter, ~50 contract tests), but `process` is defined
#       as pipelines that own no claims at all (every generation: process plan
#       carries scope_claims: []), so it misses the discriminator.
# Consequence, same as ethics_perimeter_plan.md: these nodes stay OUT of the V3
# closure % (read_closure counts only generation: v3) and OUT of
# check_closure_drift.py's terminal-state drift logic (it skips any plan whose
# generation != v3 -- this doc is still DISCOVERED by it like every *_plan.md,
# just not drift-checked).
# BEFORE this block existed (added 2026-09-02) the doc was the only one of 57
# plan files with no frontmatter at all, so read_closure emitted a
# `frontmatter_pending` placeholder with no `generation` key -- and BOTH the
# server rollup (serve.py gen_acc) and the client (closure.html
# `p.generation || 'v3'`) default a missing generation to v3. It was therefore
# filed under V3 by FALLBACK, never by decision.
closure_plan:
  id: preservation_snapshot
  generation: governance
  title: "Preservation Snapshot (archival option value, GOV-PRESERVE-1)"
  registered: 2026-08-14
  last_updated: 2026-09-02
  scope_claims: [GOV-PRESERVE-1]
  sibling_plans: [ethics_perimeter]
  summary: >
    Preserve enough of an ended organism -- substrate, developmental history,
    memories, commitments, embodiment, environment -- that faithful future
    reconstruction stays possible. Level 1 (birth-replay from
    (config, seed, commit, machine-class, env spec)) is BUILT and contract-gated;
    Level 2 (mid-life snapshot/resume) was spiked and is a measured NO-GO on
    full rollout. Nodes mirror the doc's own "Status table (resume primitive)".
  nodes:
    - id: "preservation_snapshot:RECON"
      title: "Recon -- existing state/provenance/replay machinery; two-fidelity-level split established"
      phase: 0
      status: done
      severity: load-bearing
      last_updated: 2026-08-14
      note: >
        Established that a REE life is a pure function of (REEConfig, seed) on
        pinned code (0/200 tensors differ across two seed-123 constructions),
        that provenance capture is mature/centralized (extend, don't rebuild),
        and that whole-organism save/load does NOT exist -- which is what forces
        the Level 1 / Level 2 split the rest of the plan is organised around.

    - id: "preservation_snapshot:INC1-RECORD"
      title: "Increment 1 -- ReconstructionRecord: tagged config serializer, integrity, append-only, bit-identical birth rebuild"
      phase: 1
      status: done
      severity: load-bearing
      unblocks_claims: [GOV-PRESERVE-1]
      depends_on: ["preservation_snapshot:RECON"]
      last_updated: 2026-08-14
      note: >
        ree-v3/ree_core/preservation/reconstruction_record.py. Contract
        tests/contracts/test_reconstruction_record.py (13). Fidelity boundary
        asserted honestly -- equivalence is pinned on birth CONSTRUCTION, not
        multi-step replay (torch.multinomial diverges across machine classes),
        so machine_class is stamped on every record.

    - id: "preservation_snapshot:INC1B-EMITTER"
      title: "Increment 1b -- preserve_life() emitter glue (opt-in, per-life)"
      phase: 1
      status: done
      severity: high
      depends_on: ["preservation_snapshot:INC1-RECORD"]
      last_updated: 2026-08-14
      note: >
        ree-v3/experiments/_lib/preservation.py; contract
        test_preservation_capture.py (3). Emission is opt-in and per-life on
        purpose -- GOV-PRESERVE-1 asks for PROPORTIONATE preservation, so
        nothing fires for every run and archive_dir is required and explicit.

    - id: "preservation_snapshot:INC1C-ARCHIVE"
      title: "Increment 1c -- archive backends (LocalArchive + S3Archive) + AES-GCM client-side encryption + content-addressing"
      phase: 1
      status: done
      severity: high
      depends_on: ["preservation_snapshot:INC1B-EMITTER"]
      last_updated: 2026-08-14
      note: >
        ree_core/preservation/archive.py; contract test_preservation_archive.py
        (9). boto3 lazy-imported so ree_core stays import-light; object key
        embeds the record sha256 so a changed record can never overwrite the
        original.

    - id: "preservation_snapshot:INC1C-MULTI"
      title: "Increment 1c -- MultiArchive fan-out (>1 copy) + s3_archive_from_env + storage runbook"
      phase: 1
      status: done
      severity: medium
      depends_on: ["preservation_snapshot:INC1C-ARCHIVE"]
      last_updated: 2026-08-14
      note: >
        Contract test_preservation_multi.py (5); runbook
        evidence/planning/preservation_storage_runbook.md. A record is ~10 KB,
        so cost does not discriminate between providers -- the decision is "how
        many copies" (LOCKSS / 3-2-1), which is what the fan-out implements.

    - id: "preservation_snapshot:INC1D-TOKEN"
      title: "Increment 1d -- physical-token exporter (engraveable key line + QR + gz record + manifest + README)"
      phase: 1
      status: done
      severity: medium
      depends_on: ["preservation_snapshot:INC1-RECORD"]
      last_updated: 2026-08-14
      note: >
        ree_core/preservation/token.py; contract test_preservation_token.py (7),
        including gz record re-inflates -> verifies -> reconstructs
        bit-identical. Targets the 132-byte key tier (engraved metal) and the
        Piql/Svalbard deposit tier.

    - id: "preservation_snapshot:INC1F-AUTOFIRE"
      title: "Increment 1f -- auto-fire at end-of-life (default-off REEConfig designation; fires on the abnormal path too)"
      phase: 1
      status: done
      severity: load-bearing
      depends_on: ["preservation_snapshot:INC1B-EMITTER"]
      last_updated: 2026-08-16
      note: >
        ree_core/utils/config.py + experiments/_lib/preservation.py life_scope();
        contract test_preservation_autofire.py (18, roughly half negative
        controls). The point is not sugar: an explicit end-of-driver
        preserve_life() call is exactly the line a driver that RAISES never
        reaches, so the lives most worth preserving were the ones silently
        dropped. KeyboardInterrupt/SystemExit included deliberately. Default-off
        is a HARD no-op, which is what let it land on main.

    - id: "preservation_snapshot:STORAGE-PLAN"
      title: "European-sovereign storage plan -- tiered stack documented (Hetzner / 2nd EU vendor / Zenodo + Software Heritage / Piql)"
      phase: 1
      status: done
      severity: medium
      last_updated: 2026-08-14
      note: >
        Requirement (user, 2026-08-14): entirely European-owned/-domiciled
        providers; US-owned clouds excluded even in an EU region (CLOUD Act
        reaches the company, not the datacentre). The GitHub evidence/ tree is a
        WORKING copy under US jurisdiction, not a preservation copy.

    - id: "preservation_snapshot:STORAGE-DEPLOY"
      title: "Provision the live copies -- Hetzner bucket + second-vendor bucket + Zenodo/Software Heritage deposit flow"
      phase: 2
      status: open
      severity: high
      depends_on: ["preservation_snapshot:INC1C-MULTI", "preservation_snapshot:STORAGE-PLAN"]
      blocking_on: "operational -- needs the user's provider account plus a generated encryption key held independently of the archives"
      resume_condition: >
        Account + independently-held key exist; then follow
        preservation_storage_runbook.md. Until then every built backend is
        exercised only against LocalArchive and injected fakes, so no record has
        a durable off-Mac copy.
      last_updated: 2026-08-14

    - id: "preservation_snapshot:INC2-SPIKE"
      title: "Increment 2 de-risking spike -- cost/feasibility measured on the cheapest store plus both worst cases"
      phase: 2
      status: done
      severity: load-bearing
      depends_on: ["preservation_snapshot:INC1-RECORD"]
      last_updated: 2026-08-15
      note: >
        chip-20260815-preserve-midlife-spike; contract
        test_preservation_midlife_spike.py (10, green). Deliberately added NO
        capture/restore code to the substrate -- every restore helper is local
        to the test file -- so the fleet carries zero new executable surface
        while the gate below is undecided. Key findings: `centering` reads as
        config-derived but gates cue-key arithmetic (so restore needs a
        config-IDENTITY check, not just a round-trip); the residue_field EWC
        anchor is dropped SILENTLY by state_dict, losing MECH-334 critical-period
        write-protection with a plausible loss curve; gated_policy crystallization
        is an ordered procedure, not a dict, and its naive implementation is
        wrong in the direction that looks fine.

    - id: "preservation_snapshot:INC2-ROLLOUT"
      title: "Increment 2 -- mid-life snapshot/resume, full ~10-store rollout"
      phase: 2
      status: parked
      severity: medium
      depends_on: ["preservation_snapshot:INC2-SPIKE"]
      awaiting: "a concrete queued experiment that requires mid-life resume"
      revisit_after: "the perturbation / matched-branch design in the imaging thought is queued"
      resume_condition: >
        NO-GO on the full rollout as scoped -- not infeasible (every mechanism
        was proven in a day) but the cost/reuse test is not met: measured
        1500-2000 LOC across ~12 files (majority test) plus a standing
        correctness obligation on files that changed on 28% of days over 60,
        against ZERO currently-queued experiment needing it. Increment 1 already
        discharges the owning thought's actual ask. GO NARROWLY when an
        experiment names it, building only the slice it needs:
        super_ordinal_goal_memory (free, one line), the residue_field EWC anchor
        (4 keys, proven), and the env plus its two PRNGs (the expensive,
        unavoidable one). Skip gated_policy unless the experiment crystallizes.
      last_updated: 2026-08-15

    - id: "preservation_snapshot:INC2-GUARDS"
      title: "Land regardless of the Increment 2 gate -- attribute-census contract pattern + config-identity check on any snapshot loader"
      phase: 2
      status: open
      severity: medium
      depends_on: ["preservation_snapshot:INC2-SPIKE"]
      blocking_on: "no store has acquired a loader yet, so there is nothing for the pattern to attach to"
      resume_condition: >
        Apply at the moment ANY store gains a capture/restore pair (whether or
        not INC2-ROLLOUT is un-parked). Both are cheap and both prevent a SILENT
        fidelity bug: the census forces the load-bearing-vs-telemetry fork to be
        classified rather than inspected, and the config-identity check must
        REFUSE (not warn) on mismatch.
      last_updated: 2026-08-15

    - id: "preservation_snapshot:GOV-RULE"
      title: "GOV-PRESERVE-1 registered as a candidate governance_rule on the ethics perimeter"
      phase: 1
      status: done
      severity: load-bearing
      unblocks_claims: [GOV-PRESERVE-1]
      cross_plan_link: [ethics_perimeter]
      last_updated: 2026-08-14
      note: >
        docs/claims/claims.yaml -- claim_type governance_rule, claim_level
        governance, depends_on [SENT-0, SENT-11, SENT-12]. Preservation implies
        neither immortality nor permission to revive; any future reconstruction
        needs its own governance. This node is the reason the plan sits in the
        governance lane rather than the process lane.

    - id: "preservation_snapshot:GOV-POLICY"
      title: "Open governance questions -- retention/sampling policy, create/read/re-instantiate/delete authority, reclassification trigger"
      phase: 2
      status: open
      severity: high
      depends_on: ["preservation_snapshot:GOV-RULE"]
      cross_plan_link: [ethics_perimeter]
      blocking_on: "GOV-PRESERVE-1 is `candidate`; none of its three open questions has a proposed answer"
      resume_condition: >
        GOV-PRESERVE-1's own what_would_answer names the trigger: reassess when
        (a) a retention/sampling policy is proposed (what is proportionate to
        keep, and for whom), (b) authority over create/read/re-instantiate/ever-
        delete is settled, or (c) a reclassification trigger is defined by which
        a past instance becomes "preserve with priority".
      ethical_metadata:
        welfare_relevance: potential
        requires_welfare_review: true
        applicable_ethics_gates: [SENT-0, SENT-11, SENT-12]
      last_updated: 2026-08-14

    - id: "preservation_snapshot:FISHTANK"
      title: "Memorial Fishtank -- re-instantiate preserved remnants"
      phase: 3
      status: parked
      severity: low
      depends_on: ["preservation_snapshot:GOV-POLICY"]
      awaiting: "its own governance -- re-instantiation is precisely what GOV-PRESERVE-1 declines to license"
      resume_condition: >
        Aspiration only. Blocked behind GOV-POLICY by construction: prior
        consent, privacy, identity, welfare, competing claimants and
        branching-successor moral status all have to be settled before any
        re-instantiation, and GOV-PRESERVE-1 explicitly does NOT grant
        permission to revive.
      ethical_metadata:
        welfare_relevance: high
        requires_welfare_review: true
        applicable_ethics_gates: [SENT-0, SENT-11, SENT-12]
      last_updated: 2026-08-14
---

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

**~~Deferred~~ — DONE 2026-08-16, see Increment 1f below.** The deferred item was: making a record
fire *automatically* at a boundary (end-of-life termination, Phase 2→3 via
`InfantCurriculumScheduler(on_phase3_entry=...)`, or sleep entry) via a default-off config flag plus
one call in the runner/experiment lifecycle. The end-of-life boundary is now built; the phase-entry
and sleep-entry boundaries are not (they need no new machinery — see 1f's "what is NOT built").

## Increment 1f — auto-fire at end-of-life (BUILT 2026-08-16)

**What changed.** The switch moves from the CALL SITE onto the CONFIG. Three default-off `REEConfig`
fields designate a life — `preserve_on_life_end` (bool), `preserve_archive_dir` (Optional[str]),
`preserve_on_life_end_strict` (bool) — and `experiments/_lib/preservation.py` gains the firing seam
that reads them: `life_scope(...)` (a context manager wrapping one life) and
`preserve_life_if_designated(...)` (the bare predicate + fire, for a driver that owns its own
lifecycle). A designated driver wraps its life once and never calls `preserve_life` again.

**Why this is not just sugar over the explicit call.** `preserve_life(...)` is a line at the end of a
driver, and *that is exactly the line a driver which raises never reaches*. Under the explicit form
the lives most worth preserving — the ones that ended unexpectedly — are precisely the ones silently
dropped. `life_scope` fires on the abnormal path too, stamping the cause into `reason_for_ending`
("RuntimeError: grid collapsed"). `KeyboardInterrupt` / `SystemExit` are included deliberately: a
runner SIGTERM or an operator Ctrl-C is a real way for a life to end, and a naive `except Exception`
in the exit path would have let those lives vanish unrecorded.

**Default-off is a HARD no-op, which is what let this land on `main` at all.** With
`preserve_on_life_end` False nothing is captured, no destination is resolved, and the filesystem is
not touched — the fields are read only by `experiments/_lib/preservation.py`, never by `REEAgent` or
any hot path, so an undesignated run is byte-identical to the pre-2026-08-16 substrate. That matters
because `main` is what every cloud worker pulls.

**Two error classes, deliberately handled OPPOSITELY** (pinned as a pair, so a later simplification
collapsing them fails loudly rather than silently):

| class | examples | policy | why |
|---|---|---|---|
| **misconfiguration** | designated with no destination, no seed, or two destinations | **always raises**, non-strict included | somebody designated this life; a silent skip is indistinguishable from never designating it, which is the one outcome the designation exists to rule out |
| **failed write** | full disk, unreachable bucket, duplicate `record_id` | warns and continues (`preserve_on_life_end_strict=True` inverts) | auto-fire runs at the very end of a *completed* run; a preservation problem must not convert a PASS into an ERROR |

Strict mode is itself downgraded to a warning when the life is **already unwinding**, so a
bookkeeping failure can never displace the cause of death that the driver and the runner need to see.

**Proportionality (GOV-PRESERVE-1) is preserved, not weakened.** This is a per-life *designation*,
not a fleet switch: there is still no default destination, still nothing blanket, and credentialed
backends (`S3Archive` / `MultiArchive`) are passed to the seam as `archive=` rather than put in a
config that gets serialized verbatim into every record it writes.

**What is NOT built, and why that is the right scope.** `experiment_runner.py` is untouched. It
spawns drivers as **subprocesses** and never holds a config, a seed or an agent, so it could not fill
a record even in principle — wiring there would be a fleet hot-path change with no capability gain.
The Phase 2→3 and sleep-entry boundaries are likewise not wired: both are ordinary call sites inside
a driver, so `preserve_life_if_designated(config=cfg, ...)` already serves them with no new
machinery, and pre-wiring a hook nobody has asked for would be the blanket preservation
GOV-PRESERVE-1 rules out.

Contract: `ree-v3/tests/contracts/test_preservation_autofire.py` (18 tests — default-off, hard-no-op
under both entry points, enabled writes a reconstructable record, seed falls back to `config.seed`,
explicit destination beats config, exception / KeyboardInterrupt paths, explicit reason not
overwritten, the three always-raise misconfigurations, warn-vs-strict on a failed write, strict never
displacing the cause of death, and two negative controls that the scope never suppresses the life's
own exception). Roughly half are negative controls, because the disabled pole is the load-bearing
half of this gate.

---

## Increment 2 — mid-life snapshot/resume (SPIKED 2026-08-15 → NO-GO on full rollout, narrow GO on demand)

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

### De-risking spike (RUN 2026-08-15 — results and the decision are in the next section)
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

### De-risking spike — RESULT (2026-08-15, `chip-20260815-preserve-midlife-spike`)

**Ran. Verdict: NO-GO on the full ~10-store rollout for now; GO on a narrow 3-store slice, and only
once a specific experiment needs it.** Artifact: `ree-v3/tests/contracts/test_preservation_midlife_spike.py`
(10 tests, green). The spike deliberately added **no** capture/restore code to the substrate — every
restore helper is local to the test file — so the fleet carries zero new executable surface while the
gate below is undecided, and the file can be promoted or deleted wholesale.

**1. Cheapest store (`SuperOrdinalGoalMemory`) round-trips bit-identically — and that is the smaller
half of the cost.** Wiring the existing `state_dict`/`load_state_dict` into a whole-organism walker is
literally one line (S1, S5, confirmed through two real `REEAgent` instances). What the spike actually
cost was the *fork decision*: the store has **19 instance attributes**, of which 6 are restored, 6 are
config-derived, and 7 are telemetry. Nothing in the code marks which is which. So the reusable output
is not the round-trip test but the **attribute census** (S2): the three sets are pinned, and a new
attribute on the store fails the contract until someone classifies it. That is the pattern to copy
per store, and it is ~40–80 lines of test against ~1–30 lines of capture/restore.

**2. `centering` is the trap, and it is the finding that most changes the design.** It reads as
config-derived (so `state_dict` correctly omits it) but it *gates the cue-key arithmetic*. Restoring a
centered snapshot into a store built with centering OFF is accepted without complaint and returns a
**different match for the same query** (S4, asserted). So "config-derived" does not license dropping:
every store's restore needs a **config-identity check** alongside its round-trip, and the whole-organism
loader needs to refuse (not warn) on a config mismatch. Cost: one shared mechanism, not per-store.

**3. Worst case A — `residue_field` EWC anchor — is worse than "capture-only", and cheap to fix.**
`snapshot_ewc_anchor()` does not return the anchor at all; it returns *telemetry* (`anchored`,
`n_active_centers`, `fisher_sum`) and stores the three tensors plus a bool as **plain attributes on an
`nn.Module`**. `state_dict()` therefore drops them **silently**: a naive save→load succeeds under
`strict=True`, and the restored organism's `ewc_penalty()` returns exactly `0.0` because
`_ewc_anchored` is False — i.e. it **loses its MECH-334 critical-period write-protection and keeps
training, with no error, no warning, and a plausible loss curve** (S6, asserted). The restore is
4 keys and two ~3-line helpers, proven bit-equal on the penalty itself, not just on fields (S7).
Same field also drops `_harm_history` (a plain `List[Tensor]`) while the two registered buffers beside
it survive — the asymmetry is invisible at the call site (S7b), which is exactly why the census
(finding 1) rather than inspection is the method.

**4. Worst case B — `gated_policy` crystallization — is the one that does not reduce to data.** Two
distinct failure modes (S8, both asserted): the lazy `expansion` submodule makes a strict load fail
**loudly** (`RuntimeError`, unexpected keys) *and* — force it through by rebuilding `expansion` first,
the obvious fix — the `requires_grad=False` freeze is **not part of `state_dict` at all**, so the
crystallized discrimination silently thaws and diversity gradient resumes overwriting it. Restoring
this store is an **ordered procedure** (rebuild submodule → load tensors → re-apply the freeze →
restore `_crystallized`), not a dict. Sizing note: the naive implementation of this store is silently
wrong in the direction that *looks fine*, and no round-trip test on tensor equality would catch it —
only a `requires_grad` assertion does.

**5. Cost estimate (measured, not guessed).** Live-mutated instance attributes, counted statically per
store (attributes assigned outside `__init__`, i.e. state that actually moves during a life):

| | live-mutated attrs | save | load |
|---|---|---|---|
| `super_ordinal_goal_memory` | 13 | `state_dict` | `load_state_dict` |
| `goal_state` | 7 | `state_dict` | `load_state_dict` |
| `incentive_bank` | 2 | `state_dict` | `load_state_dict` |
| `serotonin` | 5 | `get_state` | `load_state` |
| `residue_field` | 13 | `snapshot_ewc_anchor` (partial) | — |
| `gated_policy` | 9 | `get_state` (diagnostic) | — |
| `visitation_counter` | 1 | — | — |
| `anchor_set` | 2 | — | — |
| `staleness_accumulator` | 2 | `snapshot` | — |
| `ghost_goal_bank` | 1 | — | — |
| **10 stores subtotal** | **55** | 4 of 10 have a loader | |
| **env `CausalGridWorld`** | **113** | — | — |
| **total** | **168** | | |

Read that table's last two rows first: **the environment alone is twice the entire agent-side surface**
(113 vs 55), has no serializer of any kind, and additionally carries two live `np.random.default_rng`
bit-states. On the measured telemetry ratio from the one store that has been forked properly (7 of 13
live-mutated attrs were telemetry, ~54%), ~77 of the 168 are plausibly load-bearing — but that ratio is
extrapolated from a single store and is the least trustworthy number here.

Extrapolating the spike's own effort at ~100 lines per store (≈70% of it contract): **~1000 lines for
the 10 stores, plus 300–500 for the env, plus ~30 for RNG capture, plus ~20 optional analog modules
that expose `get_state()` with no setter.** Call it a **1500–2000 line change, majority test, spread
across ~12 files that no single contract currently covers.**

**6. The maintenance tax is the real cost, and it is measurable.** Over the 60 days to 2026-08-15 the
five store-bearing files took **24 commits** (`causal_grid_world.py` 13, `residue/field.py` 6,
`goal.py` 4, `serotonin.py` 1, `gated_policy.py` 0), changing on **17 of 60 days (~28%)**. Every one of
those is a potential new attribute needing a fork decision, and finding 3 establishes that getting it
wrong fails **silently**. So the recurring cost is not "keep the tests passing" — it is a standing
correctness obligation on the most actively-developed part of the substrate, at roughly a
once-every-three-days cadence.

### Decision gate — go/no-go

**NO-GO on the full rollout as scoped.** Not because it is infeasible (every mechanism was proven in a
day) but because the cost/reuse test in the original gate is not met: 1500–2000 lines and a standing
28%-of-days correctness obligation, against **zero currently-queued experiment that requires mid-life
resume**. Increment 1 (birth-replay) already discharges the owning thought's actual ask — preserving
the possibility of future reconstruction — and does so with no per-store maintenance at all.

**GO, narrowly, when a concrete experiment names it.** The perturbation / matched-branch design in the
imaging thought is the only identified consumer. When it is queued, build **only** the slice it needs
and stop: `super_ordinal_goal_memory` (free, one line), the `residue_field` EWC anchor (4 keys, proven),
and the env + its two PRNGs (the expensive, unavoidable one). Skip `gated_policy` unless the experiment
crystallizes, since it is the only store whose restore is a procedure rather than a dict.

**Two things worth landing regardless of the gate, because they are cheap and prevent silent error:**
(a) the **attribute-census contract pattern** (S2) on any store that acquires a loader; (b) a
**config-identity check** in whatever loads a snapshot, per finding 2. Neither requires committing to
Increment 2.

**Unchanged from the original scoping, and re-confirmed by the spike:** there is no single seam giving
full fidelity for free, and `agent.state_dict()` carries none of these stores (asserted in S5).

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
| Auto-fire at end-of-life (default-off `REEConfig` designation; fleet-touching) | **done + contract (18)** | `ree_core/utils/config.py`, `experiments/_lib/preservation.py`, `tests/contracts/test_preservation_autofire.py` |
| Increment 2 de-risking spike | **done + contract (10)** | `tests/contracts/test_preservation_midlife_spike.py` |
| Increment 2 (mid-life snapshot/resume) | **NO-GO on full rollout** (cost measured: ~1500-2000 LOC + 28%-of-days maintenance, no consumer queued); narrow GO when an experiment names it | this doc, §"De-risking spike — RESULT" |
| Memorial Fishtank (re-instantiate remnants) | aspiration; needs its own governance | — |
