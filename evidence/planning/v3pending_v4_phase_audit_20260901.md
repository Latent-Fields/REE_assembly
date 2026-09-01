# V3-Pending / V4-Phase Override Audit (per-claim, follow-on to GOV-V4CUT-1 F4/F5)

- **Generated:** 2026-09-01
- **Session:** metaworker-chip-20260901-v3pending-v4-phase-audit
- **Chip:** chip-20260901-v3pending-v4-phase-audit
- **Posture:** AUDIT REPORT, same posture as `v4_prerequisite_cut_20260901.md` -- a derived
  projection over the live registry. Nothing here is a second hand-maintained registry; every
  verdict cites the claims.yaml field state or script output it was derived from, and goes stale
  the moment those move.

## Headline finding: the "54" denominator was measuring the wrong thing

GOV-V4CUT-1 F4 (chip-20260901-v4cut-f4-arc080-object-identity-ownership) found that
`v3_pending: true` acts as an override in `scripts/build_claims_json.py:resolve_assembly_state`,
bucketing a claim into `gated_v3` regardless of `implementation_phase`. The orchestrator then
measured "54 claims carry `implementation_phase: v4` AND `v3_pending: true`" and dispatched this
audit against that count (re-measured at session start: still 54, unchanged from the brief).

**That count is not the same predicate as "affected by the F4 override bug".** Reading
`resolve_assembly_state`'s branch order line by line:

```python
elif epi == "substrate_conditional": state = "awaiting_substrate"   # checked BEFORE v3_pending
elif epi == "substrate_ceiling": state = "enriching"
elif v3p: state = "gated_v3"                                        # the override F4 found
```

`epistemic_category == "substrate_conditional"` is checked, and short-circuits, **before** the
`v3_pending` override branch is ever reached. Running the real resolver
(`build_claims_json.resolve_assembly_state`) over all 54 claims:

| resolved `assembly_state` | count |
|---|---|
| `gated_v3` (the F4 bug shape) | **2** |
| `awaiting_substrate` (v3_pending is inert here) | **52** |

52 of the 54 carry `epistemic_category: substrate_conditional` and therefore **never reach the
v3_pending override at all** -- clearing `v3_pending` on them would be a byte-identical no-op for
`assembly_state` today. The same is true of the independent governance-testability check in
`generate_inter_governance_workset.py` (`_claim_v3_testable`-style logic, ~line 1062): it treats
`v3_pending` and an untestable `epistemic_category` (`substrate_ceiling`/`substrate_conditional`)
as **independent, redundant** disqualifiers -- either alone already suppresses readiness. So for
the 52, `v3_pending` currently has **zero observable effect** on any live code path.

**Corrected live population: 2, not 54.** Both are already correctly, deliberately adjudicated
(see Bucket A). The gated_v3 denominator this audit could move by editing `v3_pending` is 0
today's edits change 0 live `gated_v3` memberships, because the two live members were already
right and the other 52 were never live members to begin with.

Verified this is not a general amnesty: re-running the same resolver over the F4 fix targets
(ARC-080/081/082/083, `v3_pending` already `false`) confirms their **pre-fix** `epistemic_category`
was `substrate_coherence`/absent -- not `substrate_conditional`/`substrate_ceiling` -- so F4's fix
was a genuine live-effect correction, not a dormant one. The two audits are consistent; this is a
denominator refinement for the *current* residual population, not a retraction of F4.

## Method

Per the brief's instruction to follow F5's method (`v4_prerequisite_cut_20260901.md` Section 3,
F5; `GFLAG-0105`/`GFLAG-0112`/`GFLAG-0113`): judge each claim against its own content and actual
substrate, never against cohort membership or the shape of the flag pair. Evidence gathered per
claim:

1. `resolve_assembly_state` (does `v3_pending` even reach live effect for this claim?).
2. `scripts/check_claim_phase_consistency.py --json` (does a real, currently-registered V3 build
   commitment `depends_on`/`emergent_from` this claim, independent of its own `v3_pending` flag?).
3. `live_status.evidence.verdict` and inline `phase_locked` comments in claims.yaml (has this
   *specific* claim already been through a governance/reconciliation adjudication?).
4. `evidence_quality_note` / `notes` / `functional_restatement` text (does the claim self-declare
   V4-only scope, or a "DO NOT build in V3" caveat?).
5. Grep of `ree-v3/ree_core/` for substrate the claim's content would require, for claims whose
   content names a structural V4 primitive (mirrors GFLAG-0105's own verification method).
6. `evidence/planning/substrate_queue.json` `unblocks_claims` (is there a real, tracked build item
   this claim is actually waiting on?).

## The GFLAG-0112-style pattern check ("does the same edge explain several of the 50?")

GFLAG-0112 found ARC-059's `depends_on` breadth mechanically dragging MECH-274/278 into a v3
label. No single `depends_on` edge produces the same effect here -- `phase_derived_from` is null
and `phase_provenance` is `assigned` (not `derived`) for every one of the 54, so none of them
inherited their `v4` phase mechanically through a dependency edge.

**But a different, equally mechanical pattern explains 52 of the 54: a shared REGISTRATION
TEMPLATE, not a shared dependency edge.** `.claude/skills/thought-ingestion/SKILL.md` (the
skill that registered the large majority of these) documents, as its own worked example, exactly
three of this audit's claims (`ARC-128`, `MECH-497`, `MECH-498`) and states the default template
explicitly: `epistemic_category` "almost always `substrate_conditional` for a freshly ingested
architectural idea with no substrate built yet" (line 138) and `implementation_phase` "default
`v4`... unless the thought is cleanly and cheaply testable on substrate that already exists in V3
*today*" (line 141). The skill never mentions `v3_pending` at all -- but its Step-4 instruction to
"shape each entry on a recent comparable example" (line 128) is exactly the mechanism by which
`v3_pending: true` propagated alongside the two documented fields into every new registration,
without being an independent per-claim judgment call. Registration-batch grouping in the
`notes` fields confirms this: e.g. the 2026-08-12 `persistence_must_earn_continuation` intake
alone produced `ARC-128`, `MECH-497`, `MECH-498`, `MECH-501`, `MECH-502`, `MECH-515`; the
consolidation-faults intake produced `MECH-391/392/393/401`, `INV-079/080`; the ACh/PV/BDNF
plasticity-gain intake produced `ARC-093`, `MECH-398/399/400`, `Q-072`.

This is the audit's own answer to the "if the same edge explains several of your 50, say so"
instruction: **the mechanism is a copy-forward registration convention, not a dependency edge**,
and it explains the 52-claim `substrate_conditional` cohort, not the 2-claim `gated_v3` cohort
(which predates the convention and was individually, explicitly adjudicated -- see Bucket A/B).

## Per-claim verdict table (all 54)

| Bucket | n | Verdict | Disposition |
|---|---|---|---|
| **A** -- LIVE `gated_v3`, already adjudicated | 2 | KEEP, no change | `MECH-265`, `MECH-325` |
| **B** -- dormant, chip-reviewed + `phase_locked` | 5 | KEEP, no change | `MECH-390`, `ARC-092`, `MECH-392`, `INV-080`, `MECH-401` |
| **C** -- dormant, CORRECTED this session | 3 | `v3_pending: false` applied (pending claim clearance -- see Status) | `INV-102`, `MECH-504`, `MECH-515` |
| **D** -- dormant, dependency-justified | 12 | KEEP, no change; route to `/claim-synthesis` per F1/F4 pattern | `ARC-091`, `ARC-133`, `ARC-134`, `MECH-385`, `MECH-388`, `MECH-434`, `MECH-499`, `MECH-500`, `MECH-520`, `MECH-521`, `MECH-522`, `Q-077` |
| **E** -- dormant, self-declared V4, not yet locked | 2 | NOT CHANGED here; recommend chip-20260810-style lock pass | `MECH-432`, `MECH-433` |
| **F** -- dormant, unreviewed | 30 | NOT CHANGED here; needs individual governance read | see list below |

### Bucket A -- LIVE `gated_v3`, already adjudicated (KEEP)

Both resolve to `assembly_state: gated_v3` **today**, under the actual F4 bug mechanism. Both
carry `live_status.evidence.verdict: held_v4_by_architectural_commitment/applied`, sourced from a
**user-confirmed** decision (`decision_log.v1.jsonl`, `2026-06-06T07:53:48Z`, actor `dgolden`, via
`AskUserQuestion`): *"claim is v3_pending AND implementation_phase=v4 -> deliberately V4-deferred
by architectural commitment, not awaiting V3 substrate... per the 2026-04-27 misclassification
fix."* This is documented governance doctrine, not an oversight: `docs/architecture/
v3_v4_phase_substrate_boundary.md` (registered 2026-04-26) explicitly anticipates this exact
labelling shape for its held cluster and states the intended fix is to teach the **governance
pipeline's recommendation text** to say `held_v4_by_architectural_commitment` instead of
`hold_pending_v3_substrate` -- **not** to clear `v3_pending` on the claim. Both claims' own
`notes` state "V3 implication: do NOT implement. V4-scope mechanism" (MECH-265) / an explicit
V4-target-architecture scope confirmed against ARC-072 (MECH-325).

- **MECH-265** (frontopolar relative-importance monitoring, SD-033e). `phase_locked: true`,
  comment cites SD-033e's own 2026-08-07 reclassification_note: "MECH-265 relative-importance is
  structurally V4-blocked (single-resource env, no K>=2 goals)". Checker flags a `CONFLICT`
  (SD-033e depends_on MECH-265) -- already known and accepted; SD-033e's v3 slice does not
  actually use MECH-265 (functions 1+4/MECH-264 only).
- **MECH-325** (hippocampal cue-indexed trajectory library). `phase_locked: true`, comment notes
  the ARC-072->MECH-325 edge that had driven an earlier reclassification was itself reversed
  2026-08-10; own notes: "describes the target architecture... BEYOND V3... explicit V4 target-
  architecture scope."

**Verdict: no action.** These are the F4-bug SHAPE without being the F4-bug SUBSTANCE -- exactly
the caution the brief raised about MECH-276 in GFLAG-0105, mirrored here in the opposite
direction (label pattern matches a bug signature, but the individual claim was independently,
correctly adjudicated before this audit ran).

### Bucket B -- dormant, chip-20260810-reviewed + `phase_locked` (KEEP)

`grep -c "chip-20260810-phase-consistency-reconciliation" claims.yaml` finds 30 claims touched by
that reconciliation chip; 5 of them (plus Bucket A's 2) are in this audit's 54. All 5 carry
explicit inline comments citing their own `notes` ("intrinsic V4 scope... DO NOT build in V3") and
`phase_locked: true`, set in the same 2026-08-10 pass as Bucket A:

- **MECH-390** (affect-vector developmental sparsification) -- "substrate_conditional on a V4
  affect substrate not yet built. DO NOT build in V3."
- **ARC-092** (imagination-learning constraint) -- checker flags `CONFLICT` (direct_drivers
  MECH-525, MECH-526); already reviewed and locked despite the dependency, same shape as MECH-265.
- **MECH-392, INV-080, MECH-401** (consolidation provenance/rollback, raw-episode preservation,
  gated-write-authority) -- all three: "intrinsic V4 scope: memory_lifecycle_v4 cluster, needs the
  not-yet-built V4 memory-lifecycle store."

**Verdict: no action.** Already individually reviewed 2026-08-10; not part of the unreviewed
residue.

### Bucket C -- dormant, CORRECTED this session (multi-agent, zero V3 substrate path)

These three are structurally identical in kind to GFLAG-0105's confirmed finding for MECH-274/
ARC-031 (multi-agent-requiring content = definitionally V4, zero substrate exists). Verified
directly rather than inferred from cohort shape, per the brief's central caution:

```
$ grep -rli "other.agent\|multi.agent\|other_agent" ree-v3/ree_core/
ree_core/utils/config.py   # one hit: a comment reading "V5 multi-agent social synchronisation
                            # experiments" -- no actual multi-agent substrate
```

Zero multi-agent substrate exists anywhere in `ree-v3/ree_core` (matching GFLAG-0105's own
verification for MECH-274 verbatim). No checker-found V3 driver depends on any of the three.

- **INV-102** -- "In a world containing other predictive agents, causal-model selection over an
  observation must include..." -- structurally requires another agent to exist.
- **MECH-504** -- own notes: "Fills a gap MECH-276's own notes already name but leave
  unregistered: 'a V4 social-intervention mechanism (parallel to MECH-278 for other-agents).'"
  Self-identifies as the same V4 social-intervention class GFLAG-0105 already relabeled MECH-278
  into.
- **MECH-515** -- "In multi-agent settings, the cost of continued deliberation..."; depends_on
  `INV-102` (this same bucket).

**Verdict: `v3_pending: false` (matches the F4/GFLAG-0105 disposition for the same content
class).** Zero live effect today (both `assembly_state` and governance testability are already
suppressed via `epistemic_category: substrate_conditional`); the value is closing the LATENT
recurrence risk -- if/when substrate work elsewhere causes `epistemic_category` to be cleared on
one of these before anyone re-examines `v3_pending`, the claim would silently fall through to the
exact F4 override bug. **Application status: see "Status of the 3 corrections" below** --
`claims.yaml` was contended by a concurrent governance session (`govapply-20260901`) for the
duration of this audit; edits are prepared but application depends on that claim clearing.

### Bucket D -- dormant, dependency-justified (KEEP, route to claim-synthesis)

`check_claim_phase_consistency.py --json` finds a real, currently-registered V3 build commitment
whose `depends_on` graph reaches each of these 12, either directly (`root`) or transitively
(`cascade`, `follows_from` the named root). This is independent, mechanical evidence that
`v3_pending` is not vestigial for this group -- a genuine V3-side dependency pressure exists in
the registry today, even though it is currently masked by `epistemic_category`.

| id | checker verdict | driver / follows_from |
|---|---|---|
| ARC-133 | RECLASSIFY (root) | MECH-523 |
| ARC-134 | RECLASSIFY (root) | MECH-523, MECH-531 |
| MECH-520 | RECLASSIFY (root) | MECH-523 |
| MECH-521 | RECLASSIFY (root) | MECH-523 |
| MECH-499, MECH-500, MECH-522, ARC-091, MECH-385, MECH-388, MECH-434, Q-077 | RECLASSIFY (cascade) | follows_from MECH-521 |

The root driver, **MECH-523**, is the P4 "representation-training debt" cluster the parent audit
(`v4_prerequisite_cut_20260901.md` §1, P4) ranks as one of the two highest-leverage BLOCKING V3
prerequisites, and the specific ARC-133/ARC-134/MECH-520/521/522 sub-cluster is **already** the
subject of a registered, unapplied split proposal in that same document (§3, **F1**: "ARC-134 +
MECH-521 (endogenous perceptual grain): SPLIT, minimal P0 forward... the richer mechanism
(MECH-521's occupancy-as-order-parameter settling dynamics, MECH-522 ephaptic specialisation)
stays v4_v5"). MECH-499/500/521/522 additionally overlap the pre-existing ephaptic/V4 architectural
commitment (`v3_v4_phase_substrate_boundary.md`: MECH-228, MECH-270 held-cluster) -- both
MECH-499 and MECH-522 `depends_on` MECH-228 and/or MECH-270 directly.

**Verdict: no `v3_pending` action.** The correct fix for this cluster is F1's already-proposed
claim SPLIT (minimal v3-testable operator vs. richer v4 mechanism), not a flag flip -- exactly
the brief's own instruction to "prefer claim SPLITS... over wholesale relabelling." Clearing
`v3_pending` here would discard a real, currently-tracked dependency signal for zero live benefit.
This is reported, not actioned; routing to `/claim-synthesis` is out of this audit's scope.

### Bucket E -- dormant, self-declared V4, not chip-locked (report only)

- **MECH-432, MECH-433** (dACC<->FPC arbitration loop; LC-NE explore/exploit gain) -- both
  `evidence_quality_note`: "Registered pre-implementation (V4 scope), literature-grounded only
  (PROMOTES NOTHING; experimental_confidence stays 0)" -- the identical registration style Bucket
  A's MECH-265 uses, in the same Prong-D PFC lit-pull cluster (MECH-432 `depends_on` MECH-265
  directly). Not run through the 2026-08-10 reconciliation chip, so not yet `phase_locked`.

**Verdict: not changed in this pass.** High-confidence candidates for a `phase_locked: true` pass
matching their siblings (MECH-265's exact cluster), but this audit did not independently re-derive
the literature grounding the way it did for the multi-agent trio (Bucket C) -- flagged for
governance rather than applied, per the brief's confidence threshold.

### Bucket F -- dormant, unreviewed (report only, no individual verdict)

30 claims: `INV-078`, `MECH-386`, `MECH-387`, `Q-070`, `MECH-435`, `MECH-389`, `MECH-391`,
`MECH-393`, `INV-079`, `SD-060`, `MECH-394`, `Q-071`, `MECH-396`, `MECH-397`, `ARC-093`,
`MECH-398`, `MECH-399`, `MECH-400`, `Q-072`, `Q-076`, `MECH-425`, `ARC-128`, `MECH-497`,
`MECH-498`, `ARC-129`, `MECH-501`, `MECH-502`, `SD-101`, `MECH-503`, `MECH-519`.

None carry a checker-found V3 driver, a chip-reconciliation lock, or an unambiguous structural
V4-only marker (no multi-agent requirement verified against substrate the way Bucket C was). Their
`v3_pending` is consistent with the same registration-template mechanism identified above
(epistemic_category `substrate_conditional` set explicitly per `thought-ingestion` SKILL.md
convention; `v3_pending` copy-forwarded alongside it), but **that inference alone is not
sufficient to declare a "clear-cut correction" per claim** without reading each one's specific
content and dependency context individually -- exactly the cohort-based reasoning the brief warns
against (the MECH-276 lesson). All 30 are currently inert (zero live `assembly_state` or
governance-testability effect), so there is no urgency; recommended as a follow-on `/claim-
synthesis`-adjacent review, not a stop-the-line item.

## Status of the 3 corrections (Bucket C)

`REE_assembly/docs/claims/claims.yaml` was held by an active, non-stale claim
(`govapply-20260901`, "apply approved flag dispositions: ARC-004 narrowing, replay/consolidation
family D1-D4, Q-042 promotion, standalone flags 0051/0080/0085/0091") for the full duration of
this audit; `task_claim.py open`/`check` both returned `CONTENTION_EXIT` naming that session as
owner. Per CLAUDE.md's claim-arbitration rule ("If you are told you are NOT the owner: stop... put
what you learned in the completion_note"), this audit did not write to `claims.yaml`.

**The 3 proposed edits, ready for whoever next holds the claim:**

```yaml
# INV-102 -- change v3_pending: true -> false (line: grep "^- id: INV-102$" claims.yaml)
# MECH-504 -- change v3_pending: true -> false
# MECH-515 -- change v3_pending: true -> false
```

No other field changes proposed (leave `implementation_phase: v4`, `epistemic_category:
substrate_conditional` untouched -- only the redundant/latent-risk `v3_pending` flag moves).

## Answer to "how much did the gated_v3 denominator actually move"

**By zero, and that is the finding.** The live `gated_v3` population attributable to this override
pattern was never 54 -- it was 2, and both were already correct before this session started. The
54-count conflated a 2-claim live bug-shaped cohort with a 52-claim dormant cohort produced by an
unrelated, already-documented registration convention. No `gated_v3` membership changes as a
result of this audit; 3 `v3_pending` flags move on dormant (non-`gated_v3`) claims as a prophylactic
fix, pending claims.yaml contention clearing.

## Reproducibility

```bash
# Population (re-run at any time; this audit's 54 was measured 2026-09-01T19:0xZ)
python3 -c "
import yaml
d = yaml.safe_load(open('docs/claims/claims.yaml'))
claims = d if isinstance(d, list) else d.get('claims', d)
mine = [c['id'] for c in claims if str(c.get('implementation_phase','')).strip().lower()=='v4' and bool(c.get('v3_pending'))]
print(len(mine)); print(mine)
"
# Live-effect split (Bucket A vs the rest)
python3 -c "
import sys; sys.path.insert(0, 'scripts')
import build_claims_json as bcj, yaml
d = yaml.safe_load(open('docs/claims/claims.yaml'))
claims = d if isinstance(d, list) else d.get('claims', d)
mine = [c for c in claims if str(c.get('implementation_phase','')).strip().lower()=='v4' and bool(c.get('v3_pending'))]
print([ (c['id'], bcj.resolve_assembly_state(c)[0]) for c in mine if bcj.resolve_assembly_state(c)[0] != 'awaiting_substrate' ])
"
# Dependency-driver evidence (Bucket D)
python3 scripts/check_claim_phase_consistency.py --json
```

- Supersedes: nothing (first pass at this specific population).
- Superseded by: any re-run after `govapply-20260901`'s dispositions land (that session's
  standalone-flag work is disjoint from this audit's 3 ids, but re-reading `claims.yaml` fresh
  before applying Bucket C is mandatory per the umbrella's read-modify-write rule) or after
  `/claim-synthesis` acts on Bucket D's F1 routing.
