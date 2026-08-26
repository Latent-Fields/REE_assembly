---
title: "SD-033d: Premotor/SMA-analog (sequence-execution substrate)"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 23
status: candidate
status_asof: 2026-07-10
status_claim: SD-033D
---

# SD-033d: Premotor/SMA-analog (sequence-execution substrate)

**Claim ID:** SD-033d (subdivision of the SD-033 PFC cluster)
**Subject:** `pfc.premotor_sma_analog_sequence_execution`
**Status:** candidate, `implementation_phase: v3`, `v3_pending: false`
**Registered:** 2026-04-19
**Design doc written:** 2026-06-09 (commitment_closure:GAP-9 — the registration
carried `design_doc: null` until this pass)
**Instantiates:** SD-033 (PFC subdivision cluster)
**Depends on:** SD-033, SD-033a, MECH-094, MECH-261, MECH-090, ARC-028

---

## What this document is

SD-033d is a **registration-only graph-completeness subdivision**. The premotor /
SMA sequence-execution function it names is **already implemented** inside ree-v3's
E3 trajectory machinery and the MECH-090 commitment loop. This document does the
GAP-9 task: it **maps the existing machinery onto the premotor/SMA biology** so the
SD-033 claim graph mirrors the primate frontal-lobe parcellation rather than
implying a premotor-less architecture. **No new substrate is proposed and none is
required.** If you are looking for a module called `premotor_sma_analog.py`, there
is deliberately none — the point of this doc is that the function is distributed
across modules that already exist.

The companion parent doc is
[`sd_033_pfc_subdivision_architecture.md`](./sd_033_pfc_subdivision_architecture.md);
this doc expands the one-paragraph SD-033d subdivision entry there into the full
machinery mapping.

---

## The biology being mapped

Tanji & Hoshi 2008 (*Physiol Rev*, "Role of the lateral prefrontal cortex in
executive behavioral control") describe a graded executive-control axis running
caudally from lateral PFC:

| Region | Function (Tanji & Hoshi 2008) |
|---|---|
| **Lateral PFC** | Holds the abstract rule / goal that the sequence serves |
| **pre-SMA** | Sequence *planning*, set-switching, ordering of forthcoming actions |
| **SMA proper** | Sequence *execution* — unrolling a committed motor program step by step |
| **Dorsal premotor (PMd)** | Stimulus→action binding (selecting the action a state affords) |

The rostro-caudal gradient is: abstract rule (lateral PFC) → ordered plan (pre-SMA)
→ executed program (SMA) → stimulus-bound action (PMd). REE's
**SD-033a → SD-033d** relation captures the **rule → sequence-execution** segment of
this gradient: SD-033a (lateral-PFC-analog) holds the rule/goal; SD-033d is
everything downstream that turns that context into an executed action sequence.

---

## The mapping: existing ree-v3 machinery → premotor/SMA biology

Every row below is **already in the codebase**. SD-033d is the claim-graph name for
their collective premotor/SMA role.

| Biological role | ree-v3 component | Location |
|---|---|---|
| **PMd — stimulus→action binding** (which action does this state afford?) | `HippocampalModule.propose_trajectories()` generates candidate action sequences from the current state; `E2FastPredictor.action_object()` is the affordance map the proposer navigates | `ree_core/hippocampal/module.py:857`, `ree_core/predictors/e2_fast.py` |
| **pre-SMA — sequence planning / ordering / set-switching** | `E3TrajectorySelector.select()` scores the multi-step candidate trajectories and picks the one to commit; the diversity / authority machinery (ARC-065 SP-CEM, MECH-341) keeps the candidate plan-set from collapsing to a single ordering | `ree_core/predictors/e3_selector.py:73` |
| **SMA proper — sequence execution** (unroll a committed program step by step, not re-decide each tick) | MECH-090 Layer-1 committed-trajectory stepping: `REEAgent.select_action` advances `_committed_step_idx` through `committed_trajectory.actions[:, idx, :]` while the bistable BetaGate holds | `ree_core/agent.py:1746` / `:3796` (the `_committed_step_idx` counter) |
| **Commitment latch — "execute this program, do not re-evaluate every cycle"** | MECH-090 bistable `BetaGate` (`beta_gate_bistable`): elevates on commit-entry, holds through execution | `ree_core/heartbeat/beta_gate.py` |
| **Sequence-end / program-complete signal → release** | ARC-028 + MECH-105: `HippocampalModule.compute_completion_signal()` → `BetaGate.receive_hippocampal_completion()` releases the latch at sequence end (Lisman & Grace subiculum→NAc→VTA loop) | `ree_core/hippocampal/module.py:1655`, `ree_core/heartbeat/beta_gate.py:164` |
| **Urgency abort of the running program** | MECH-091 urgency interrupt: `z_harm_a.norm() > threshold` releases the latch mid-sequence and resets `_committed_step_idx` | `ree_core/agent.py` select_action MECH-091 block |

The two halves Tanji & Hoshi separate — *planning the order* (pre-SMA) and
*executing the committed order without re-deciding* (SMA) — map cleanly onto REE's
**propose+score** stage versus the **MECH-090 committed-step stepping** stage. The
bistable BetaGate is exactly the "do not re-evaluate the program each striatal
cycle" property SMA-proper execution requires.

---

## MECH-261 write-gating profile (the SD-032 interface)

SD-033d inherits MECH-094 hypothesis-tag gating as the **specific case** of the
MECH-261 mode-conditioned registry (MECH-094 is the sequence-commit instance of the
general gate). Per the SD-033 cluster gating table:

- **external_task / internal_planning** — sequence-level writes licensed (plan and
  commit real action sequences).
- **internal_replay** — suppressed *unless* the hypothesis tag is explicitly set
  (imagined sequences must not silently overwrite the committed program; this is
  why MECH-094's `hypothesis_tag` rides on simulated trajectories).
- **offline_consolidation** — consolidative (slow updating of learned
  state→sequence mappings).

SD-033d is therefore the subdivision where MECH-094 is most visibly load-bearing:
the hypothesis tag is the gate that keeps replayed/imagined action sequences from
being executed as if real.

---

## Why register it rather than build it

REE registers the PFC as a five-subdivision cluster **up front** (the SD-010/SD-011
late-split lesson: implementing a monolith and re-splitting later is expensive). The
premotor/SMA function is genuinely present in E3 + MECH-090, so SD-033d's correct
status is *named-but-not-rebuilt*. Building a separate `premotor_sma_analog` module
would duplicate the trajectory machinery and create two competing
sequence-execution paths — the opposite of what the cluster registration is for.

`v3_pending: false` is correct: there is no deferred V3 implementation work. The
function exists; only the claim-graph name and this mapping doc were missing.

---

## Falsification / split trigger

SD-033d is **registration-only**, so it is not falsifiable at the substrate level in
the way SD-033a/b are. The load-bearing falsifications for its claimed function live
on the components it maps to (E3 trajectory experiments; MECH-090 commitment
experiments). What SD-033d *does* carry is a **split trigger**:

> If future experimental evidence shows that E3's trajectory-proposal/selection +
> MECH-090 stepping machinery **inadequately covers** the pre-SMA / SMA / PMd
> distinctions — e.g. a sequence-planning vs sequence-execution dissociation that
> the single E3-commit pathway cannot reproduce — then SD-033d should be **split**
> into `SD-033d-i` (pre-SMA planning), `SD-033d-ii` (SMA execution), `SD-033d-iii`
> (PMd stimulus-action binding) along the Tanji & Hoshi subdivisions, and the
> corresponding machinery factored apart.

Until such evidence appears, the single-subdivision registration is the parsimonious
reading.

---

## Related claims

- **SD-033, SD-033a–e** — the PFC subdivision cluster (parent + siblings)
- **SD-033a** — lateral-PFC-analog; the upstream rule/goal source SD-033d executes
- **MECH-090** — bistable commitment latch + committed-trajectory stepping (SMA execution)
- **ARC-028 / MECH-105** — hippocampal-completion → BetaGate release (sequence-end signal)
- **MECH-091** — urgency interrupt (mid-sequence abort)
- **MECH-261** — mode-conditioned write gating (SD-032a interface)
- **MECH-094** — hypothesis tag (the specific gate on sequence commits)
- **ARC-018** — waking trajectory-proposal loop (the proposer SD-033d executes)

## References

- Tanji, J. & Hoshi, E. 2008. *Role of the lateral prefrontal cortex in executive
  behavioral control*. Physiol Rev 88(1):37–57. — the lateral-PFC → pre-SMA → SMA →
  dorsal-premotor executive-control gradient this doc maps onto.
- Lisman, J.E. & Grace, A.A. 2005. *The hippocampal-VTA loop*. Neuron 46(5):703–713.
  — the completion → release loop (ARC-028 / MECH-105).
- Primary cluster lit-pull: `evidence/literature/targeted_review_pfc_subdivision_architecture/synthesis.md`.
