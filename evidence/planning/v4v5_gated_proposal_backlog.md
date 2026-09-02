# V4/V5-gated proposal chip backlog

**Purpose.** `proposal_routine_tick` mints a `chip-proposal-exp-<N>: Queue experiment for
EXP-<N> (<claim-id>)` chip for every proposal it considers "V3-testable" -- but its
`_claim_is_v3_testable()` predicate does not check `claim_type=architectural_commitment` /
`held_v4_by_architectural_commitment`, so it also mints these for claims whose
`implementation_phase` is `v4` or `v5` in `claims.yaml`. Those chips are false work orders:
no V3 experiment can be designed against a claim that has no V3 substrate and isn't scheduled
for one. Root-cause fix is tracked separately (still open) as
`chip-20260901-igw-tick-architectural-commitment-testability-gap` -- **do not duplicate that
fix here**; this doc is only the holding pen for the individual mis-minted proposal chips it
produces, so they stop cluttering the live science backlog until the predicate is fixed.

**Pulled from `TASK_CHIPS.json` on 2026-09-02** (33 chips, all `origin: proposal_tick`, all
`kind: work`, one held an active claim -- `chip-proposal-exp-0437` was claimed by session
`659e657b-0660-4614-9002-c147ed1433a0`; withdrawn anyway since the underlying claim cannot
produce a V3 experiment regardless of who holds the chip). Original chip content (title/tldr/
prompt) is preserved in each chip's own `resolution_note_history` in `TASK_CHIPS.json` --
this doc adds the claim-phase grounding that chip text didn't carry.

**Re-derivation note.** `proposal_tick` will keep re-minting these (and new ones for other
v4/v5 claims) on every tick until the root-cause chip lands. Re-run the classification query
below periodically and append newly-withdrawn chips to the matching claim's row (or a new row)
rather than opening a second copy of this doc:

```bash
python3 -c "
import json, re, yaml, collections
chips = json.load(open('TASK_CHIPS.json'))['chips']
open_chips = [c for c in chips if c.get('status')=='open' and c['chip_ref'].startswith('chip-proposal-exp-')]
id_pat = re.compile(r'\b(MECH|ARC|SD|INV|EXT|IMPL|GAP)-\d+[a-z]?\b')
claims = yaml.safe_load(open('REE_assembly/docs/claims/claims.yaml'))
phase_by_id = {c['id']: c.get('implementation_phase') for c in claims}
for c in open_chips:
    blob = c['title'] + ' ' + c['tldr']
    ids = set(m.group(0) for m in id_pat.finditer(blob))
    bad = {i: phase_by_id.get(i) for i in ids if phase_by_id.get(i) in ('v4','v5','v6')}
    if bad:
        print(c['chip_ref'], bad)
"
```

## Dependency model (applies to every row below)

- **Dependency:** the named claim's `implementation_phase` must move from `v4`/`v5` to `v3`
  (i.e. it must acquire a V3-buildable substrate and lose its `architectural_commitment` /
  `held_v4_by_architectural_commitment` hold) before any experiment against it is queueable.
  That phase transition is a governance/architecture decision, not something this backlog or
  `/queue-experiment` can trigger.
- **Implementation needed once unblocked:** design + queue via `/queue-experiment` against the
  `EXP-<N>` proposal named in each row (or its regenerated successor, since `proposal_id`s
  reshuffle on reindex -- see `chip-20260902-proposal-id-reference-rot`, also still open).
  Until then: **no action** -- these are correctly parked, not stalled.
- **Version:** the `implementation_phase` value from `claims.yaml` at time of pull.

## v5-phase (further out -- no CBF/verification substrate exists at all)

| Claim | Phase | Statement (truncated) | Withdrawn chip(s) | EXP proposal(s) |
|---|---|---|---|---|
| MECH-145 | v5 | Prescriptive ethical trajectory certification requires a Control Barrier Function (CBF) or equivalent... | chip-proposal-exp-0857 | EXP-0857 |
| MECH-146 | v5 | Diagnostic ethical trajectory verification (counterfactual case, MECH-127) requires backward... | chip-proposal-exp-0859 | EXP-0859 |

## v4-phase (architectural-commitment held; needs its own substrate generation)

| Claim | Phase | Statement (truncated) | Withdrawn chip(s) | EXP proposal(s) |
|---|---|---|---|---|
| ARC-031 | v4 | HippocampalModule navigates z_self trajectory space (deliberation sequences) in addition to z_world... | chip-proposal-exp-0433, chip-proposal-exp-0437 | EXP-0433, EXP-0437 |
| ARC-055 | v4 | Verisimilitude signal availability: V(t) and D_V must be explicitly available to E3 selection... | chip-proposal-exp-0451 | EXP-0451 -- **ROUTED 2026-09-02**: current experimental-lane proposal EXP-0448 (same EVB-1200 backlog item; EXP-0451 renumbered away on a governance regen) marked `blocked_substrate` in `experiment_proposals.v1.json` (REE_assembly `e309cde5c8`), per chip-proposal-exp-0451's own re-dispatch. No further routing owed for this row. |
| ARC-082 | v4 | Tools/affordances as object->action binding (PILLAR 3 of ARC-080)... | chip-proposal-exp-0466, chip-proposal-exp-0468 | EXP-0466, EXP-0468 |
| ARC-083 | v4 | Others-as-object (PILLAR 4 of ARC-080): each other agent gets its own token-keyed object-file slot... | chip-proposal-exp-0470 | EXP-0470 |
| INV-039 | v4 | Schema-primed rapid assimilation: any hippocampal planning system with a stable prior map must gate... | chip-proposal-exp-0676, chip-proposal-exp-0678 | EXP-0676, EXP-0678 |
| MECH-218 | v4 | interoceptive_predictive_wanting | chip-proposal-exp-0881 | EXP-0881 |
| MECH-224 | v4 | harm_eval.piecewise_gradient_structure: E3 harm_eval learns both continuous intensity and discrete... | chip-proposal-exp-0889, chip-proposal-exp-0891 | EXP-0889, EXP-0891 |
| MECH-228 | v4 | Field-level coherence support (ephaptic coupling): extracellular electric field interactions stabilise... | chip-proposal-exp-0896 | EXP-0896 |
| MECH-240 | v4 | SD-012 homeostatic drive_level dynamically scales z_goal attractor basin width... | chip-proposal-exp-0908 | EXP-0908 |
| MECH-241 | v4 | During active goal pursuit, hippocampal and OFC-analogue representations of goal-proximal states... | chip-proposal-exp-0910 | EXP-0910 |
| MECH-242 | v4 | Hippocampal trajectory construction operates via two dissociable mechanisms... | chip-proposal-exp-0912 | EXP-0912 |
| MECH-243 | v4 | A dedicated hippocampal output pathway (analogous to vCA1 to nucleus accumbens shell)... | chip-proposal-exp-0914 | EXP-0914 |
| MECH-255 | v4 | Template compilation is implemented by vmPFC value-content projection composed with dlPFC context-gating... | chip-proposal-exp-0938 | EXP-0938 |
| MECH-274 | v4 | V4-reserved. The sleep-dependent aggregation pattern of MECH-273 extends to other-attribution... | chip-proposal-exp-0932, chip-proposal-exp-0940, chip-proposal-exp-0942 | EXP-0932, EXP-0940, EXP-0942 |
| MECH-298 | v4 | Event-gated frontal write at goal-instantiation moments... | chip-proposal-exp-0943 | EXP-0943 |
| MECH-299 | v4 | Theta-cycle content scales with the agent's current substrate abstraction vocabulary... | chip-proposal-exp-0945 | EXP-0945 |
| SD-041 | v4 | An explicit thalamic-routing substrate (reuniens/MD-analogue) gates and amplifies bidirectional traffic... | chip-proposal-exp-1146, chip-proposal-exp-1155 | EXP-1146, EXP-1155 |
| SD-043 | v4 | vmPFC analogue gains an abstract task-structure encoding capacity that compresses anchor-pool geometry... | chip-proposal-exp-1148, chip-proposal-exp-1157, chip-proposal-exp-1161 | EXP-1148, EXP-1157, EXP-1161 |
| SD-044 | v4 | Motor primitive substrate at the bottom of the action-representation hierarchy... | chip-proposal-exp-1150, chip-proposal-exp-1152, chip-proposal-exp-1159, chip-proposal-exp-1163 | EXP-1150, EXP-1152, EXP-1159, EXP-1163 |

## What stayed in the live ledger (deliberately not pulled)

Two chips also named v4/v5 claims but were kept open because they are the infra/governance
work that keeps the V3 ledger clean, not mis-scoped V3 asks themselves:

- `chip-20260901-igw-tick-architectural-commitment-testability-gap` -- the actual root-cause
  fix for this whole class (patches `_claim_is_v3_testable`).
- `chip-20260902-ext009-exp0534-blocked-substrate-status` -- correctly *routes* a v5-phase
  claim (MECH-164) out of the V3 lane by marking its proposal `blocked_substrate`; that is the
  desired outcome for every row above too, once someone runs the same routing on them.
