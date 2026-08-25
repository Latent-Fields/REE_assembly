# Failure Autopsy: V3-EXQ-861f (H1 isolation) — closing the 861e producer-vs-intervention portfolio

**Generated:** 2026-08-25T18:17:31Z
**Scope:** cluster (one new target, V3-EXQ-861f, read across into the already-confirmed `failure_autopsy_861g-861h-mech180-cluster_2026-08-23`)
**Status:** confirmed
**Claims:** INV-050, MECH-180
**qid:** `inv050_mech180_861e_producer_vs_intervention_isolation`

## Why this autopsy exists

`V3-EXQ-861f` is `experiment_purpose: "diagnostic"`, PASS, self-routed
`third_drive_independent_seed_replication_confirmed`. Per the skill's blanket rule, every
diagnostic result — PASS or FAIL — needs a confirmed autopsy before governance can act on it,
regardless of whether the indexer flagged it. `check_autopsy_coverage.py` confirmed no prior
artifact covers V3-EXQ-861f; `V3-EXQ-861g`/`V3-EXQ-861h` (the other two legs of the same
GOV-FANOUT-1 portfolio) are already covered by a CONFIRMED cluster autopsy
(`failure_autopsy_861g-861h-mech180-cluster_2026-08-23`), which this session read in full per
CLAUDE.md's re-adjudication rule before writing anything.

## 1. Facts

### The duplicate-run defect (not this autopsy's subject)

V3-EXQ-861f executed **twice** from one queue entry:

| Machine | machine_class | Start | End | Elapsed |
|---|---|---|---|---|
| ree-cloud-4 | linux-x86_64-py3.10-torch2.12.0+cpu | 2026-08-23T11:45:10Z | 2026-08-23T21:00:58Z | 9.26h |
| DLAPTOP-4.local | **darwin-arm64-py3.13-torch2.12.0** | 2026-08-22T15:40:28Z | 2026-08-24T02:38:53Z | 34.97h |

The Mac's run started 20.1h into its own still-running execution — a coordinator stale-claim
reap under `COORDINATOR_STALE_HOURS=6` racing a 35h single-experiment run. This is already
chip-tracked (`chip-20260824-exq861f-duplicate-run-stale-claim-reap`, status open) and is **not**
re-diagnosed here. The two manifests were diffed byte-for-byte: every numeric field agrees to
~1e-7–1e-9 (floating-point/torch-build noise on the identical substrate pin, not a fresh seed
draw), so they are treated as **one informative leg**, not two independent replicates.

### The decisive comparison (driver's own pre-registered declared null)

Seed 271, `ARM_3_HIGH_ON`, reseeded (measurement-phase RNG reseeded immediately before
measurement) vs unreseeded (in-run control, same substrate/process/machine, legacy behaviour):

| Cell | Run 1 (ree-cloud-4) factor | Run 2 (DLAPTOP-4) factor |
|---|---|---|
| Reseeded (H1 primary) | 0.9474699862903014 | 0.9474698502080717 |
| Unreseeded (control) | 0.8844596840125855 | 0.8844595741832282 |
| 861e's recorded decisive cell | 0.8844596840125855 | (same) |

Driver's declared null (verbatim from the docstring): *"H1 SUPPORTED if the reseeded cell's
factor rises above 1.0 while the unreseeded control stays below (reproducing 861e). H1 NOT
SUPPORTED if both cells sit below 1.0 (the collapse survives RNG isolation). This is an
INFORMATIVE null."* Both cells sit below 1.0 in **both** duplicate runs, and the control
criterion (unreseeded reproduces 861e) is met. **H1 is NOT supported — informatively.**

### The self-route label is a combination-rule leftover (same class as 861g/861h)

`interpretation.label = third_drive_independent_seed_replication_confirmed` fires on the
generic "seeds are a disjoint replication set" precondition grid, independent of what the H1
discrimination itself found. It is not a *vacuous* pass (the grid preconditions really are met),
but it must not be read as "H1 confirmed." The load-bearing readout is
`discrimination.verdict_label = h1_not_supported_collapse_survives_rng_isolation`.

### A documentation error in the manifest, found while diffing the duplicates

Both manifests' own `machine_delta_readout.note` states: *"Both runs report machine_class
linux-x86_64-py3.10-torch2.12.0+cpu, so any difference is sub-machine-class."* That is **false**
for the DLAPTOP-4.local duplicate, whose own top-level `machine_class` field reads
`darwin-arm64-py3.13-torch2.12.0` — a genuinely different architecture, OS, and Python version.
The note was authored before the duplicate-run defect produced a second, differently-classed
execution and was never updated. This does not weaken anything — if anything it strengthens the
read below — but it is flagged as a hygiene item for the driver's next revision.

## 2. Claim-layer mapping

Both INV-050 and MECH-180 are tagged `standard` / `candidate` (MECH-180 also
`v3_pending: true`). All three portfolio legs (861f, 861g, 861h) are diagnostic and pinned
`evidence_direction: non_contributory` / per-claim `unknown` by construction — **none of them
vote**, and none may move claim status, confidence, or v3_pending.

## 3. Biological-reference triage

Unchanged from 861g/861h: closest mechanism is homeostatic sleep-pressure regulation
(process-S analog) scaling SWS depth/duration with prior waking novelty load, plus
novelty-triggered hippocampal replay. Not a formal-definition import; literature is present
(same corpus as the sibling cluster); no new `/lit-pull` needed.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | diagnostic isolation leg, pinned non-voting |
| Biological reference | clear | process-S / novelty-adaptive SWS+replay; lit present |
| Prerequisites | present | R1 1.0, R2 2/3, R3 1.0 both runs; substrate pin verified |
| Implementation | complete | reseed/no-reseed isolation correctly implemented |
| Environment | partial | seed 271 write-locked (constant, doesn't confound H1) |
| Measurement | adequate | in-run control bit-reproduces 861e's recorded cell |
| Integration | coupled | |
| Scale | adequate | |

**Failure-location (GOV-FAILLOC-1):** MIXED, not chargeable to REE. The H1 isolation itself
succeeded and is fully informative; the C2 grid FAIL it sits inside is the same 861e
combination-rule leftover the sibling cluster already attributed to inherited grid mechanics.

## 5. Read-across: closing the whole portfolio

Three legs, one qid:

| Leg | Queue ID | Question | Result |
|---|---|---|---|
| H1 (measurement) | V3-EXQ-861f | Is the collapse an RNG-isolation artifact? | **NOT SUPPORTED** — collapse survives reseeding |
| H3 (algorithm/substrate) | V3-EXQ-861g | Is the collapse a substrate/machine delta? | **SUPPORTED**, left alive pending machine confound |
| CONTROL (representation) | V3-EXQ-861h | Is the ContextMemory write-address lock load-bearing? | **PASSES** — not load-bearing |

861g's H3 finding (old substrate f810969 retains HIGH grading, factor 1.007, at n=10; current
substrate 17befb8c collapses to 0.884) was left "alive" specifically because 861g ran on a
different machine (ree-cloud-2) than 861e (ree-worker-1) — substrate and machine were
confounded. **861f's own in-run control resolves that confound**: its unreseeded cell
reproduces 861e's exact decisive value (abs delta 0.0 and 1.1e-7) across **three independent
machine identities** — ree-worker-1 and ree-cloud-4 (same machine_class, linux-x86_64/py3.10)
plus DLAPTOP-4.local (a genuinely different machine_class, darwin-arm64/py3.13). The current
substrate's readout is machine-invariant to ~1e-7 across an actual architecture+OS boundary,
while only one machine has ever run the historical substrate. **The divergence is attributable
to substrate, not machine.**

**Portfolio answer:** the 861e collapse is a genuine substrate change between f810969 and
17befb8c (11 intervening `ree_core` commits) — not measurement RNG, not a machine/box effect,
not the known ContextMemory write-address lock.

### The open residual, and a live inversion candidate

```
git log --oneline f810969..17befb8c46f0b7352f74a6b6e3ee4fc9715878fc -- ree_core/
```
returns 11 commits. The most suspicious is **`76cbf84` "e1: repair ContextMemory.write()
deterministic single-slot fixed point"** — a *repair* commit touching the exact same substrate
defect family (`contextmemory-write-path-addressing-degeneracy`) already flagged as corrupting
in this lineage. If that repair is what moved the readout, **the naive "regression" framing
inverts**: f810969's >1.0 grading would itself have been an artifact of the pre-repair write-path
bug, and 17befb8c's 0.884 would be the *corrected*, lower true third-drive coupling at seed 271
— not a regression at all. Secondary candidates: `1a4b6be` (modulatory-bias-selection-authority
AMEND, touches `e3_selector` action-selection upstream of ContextMemory writes) and `0911574`
(E3 last_scores pre-arbitration staleness fix, could alter which candidate action commits at
each step). This is unresolved and is scoped as a new substrate_queue entry below rather than
guessed at.

## 6. Step 7b — mechanical pre-routing checks

One fire: C2 (SD-MEL-CONSUMER and SD-MEL-PRODUCER already unblock INV-050/MECH-180 and weren't
named in the `create` recommendation). Dismissed with reason: those two entries are about the
third-drive MEL producer/consumer *capability* (already validated/built); the new entry is a
narrower, distinct diagnostic — which landed commit changed this specific numeric readout
between two historical pins — and does not duplicate either. Cross-referenced defensively in
the new entry's own `not_a_duplicate_of` field.

## 7. Step 7c — adversarial pass (self-administered, CONFIRMED)

Two objections raised and addressed rather than suppressed:

1. *The duplicate-run manifests could inflate an apparent "replication."* Addressed by treating
   them as one leg, not independent confirmatory evidence, and by deferring the infra defect
   entirely to its own already-open chip.
2. *The cross-machine-class invariance argument could overstate confidence*, given the standing
   memory that `torch.multinomial` diverges across machine classes at identical seeds. Addressed
   by NOT claiming this refutes that memory — it is an N=1 comparison on one specific downstream
   statistic (`mean_duration_factor`), which may not exercise the divergent codepath or may
   average over enough draws to wash it out — and by resolving H3 as **confirmed**, not
   **certain**, leaving the commit-bisection question explicitly open.

No contests survive; verdict CONFIRMED.

## 8. Learning extracted

- H1 eliminated: collapse survives measurement-phase RNG isolation, replicated across two
  independent executions (one an accidental cross-machine-class duplicate).
- H3 confirmed: substrate delta between f810969 and 17befb8c, with the machine confound
  resolved by 861f's own cross-machine-class control.
- The manifest's own machine-delta prose is factually wrong for the Mac duplicate (claims
  matching machine_class when the two runs are actually cross-class) — a documentation hygiene
  finding that, once corrected, makes the discrimination *more* decisive, not less.
- WHICH of the 11 intervening commits explains the delta is open, with a live possibility
  (`76cbf84`) that the correct reading inverts which pin's number was ever "right."
- `failure_autopsy_861g-861h-mech180-cluster_2026-08-23` is CONFIRMED but **not yet applied**:
  GOV-APPLY-1 confirms both claims' `live_status.evidence.from` still cite the earlier
  `failure_autopsy_V3-EXQ-861e_2026-08-21`, and V3-EXQ-861g/861h are still listed in
  `pending_review.md`'s FAIL table as of this artifact's timestamp. Governance should apply both
  confirmed artifacts together, in sequence (861e → 861g-861h-cluster → this one), so the
  citation lands on the complete portfolio read.

## 9. Routing (user-confirmed at Step 8, 2026-08-25)

- **H1:** eliminate (recommended, adopted).
- **H3:** confirm now (recommended, adopted) — machine confound resolved by 861f's own
  cross-machine-class control.
- **Substrate queue:** the autopsy's own recommendation was record-only (neither claim is
  currently blocked on this); the user instead chose to **create** a low-priority
  (`priority_suggested: 3`, `severity: degrading`) substrate_queue entry
  (`mel-f810969-vs-17befb8c-collapse-bisection`) scoping the 11-commit bisection, prioritising
  `76cbf84` first given the possible inversion. Logged to the Recommendation-Agreement Ledger.
- **Claims:** INV-050 and MECH-180 status/confidence/v3_pending unchanged on all three legs of
  this portfolio; `evidence_quality_note` updates only, per `per_claim_recommendation` in the
  companion JSON.
- **Hypothesis-space ledger:** the intended Mode B resolutions (H1 eliminated, H3 confirmed) are
  recorded in the JSON's `hypothesis_space_ledger_pending` block but **not yet written** to
  `hypothesis_space_registry.v1.json` — that file is currently owned by a concurrent active
  claim (`failure-autopsy-cluster-c-3c01c6`, V3-EXQ-948). To be applied once that claim closes.

**routing: `queue-experiment`** (the new substrate_queue entry, once picked up, is an
`/implement-substrate`-adjacent diagnostic authored via `/queue-experiment`; nothing here
demotes or promotes any claim).
