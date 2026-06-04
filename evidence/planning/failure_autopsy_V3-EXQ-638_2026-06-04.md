# Failure Autopsy -- V3-EXQ-638 (SD-057 cue-recall cue-silent)

- **Generated (UTC):** 2026-06-04T16:06:27Z
- **Scope:** single
- **Status:** confirmed (user-confirmed routing 2026-06-04)
- **Target run_id:** `v3_exq_638_scaffold_cue_recall_contact_ablation_20260604T142524Z_v3`
- **Queue ID:** V3-EXQ-638
- **Outcome / direction:** FAIL / non_contributory
- **Purpose:** diagnostic (`claim_ids = []`; substrate-readiness probe, does NOT weight governance)

> Note: the root-cause diagnosis and code fix for this FAIL were completed inline in the
> same session that landed the fix (commits `a9ef0be` token-formation + instrumentation,
> `636128a` aggregation). This artifact formalises that diagnosis into the failure-record
> the autopsy skill produces, so `/governance` has a structured handoff. The validation
> re-issue (V3-EXQ-638a) is queued (`0258238`) and running on ree-cloud-2 as of this writing.

## 1. Facts (no interpretation)

Two arms x three seeds (42/43/44), identical 634c seeding regime (drive_floor=0.9 +
benefit_threshold=0.02); the ONLY between-arm difference is the SD-057 cue-recall bridge.

Pre-registered acceptance (from manifest `acceptance{}`):

| Criterion | Definition | Result |
|-----------|------------|--------|
| C1 cue fires ON | ARM_CUE_ON P2 n_cue_recall_fires > 0 on >= 2/3 seeds | **false** |
| C2 cue silent OFF | ARM_OFF P2 n_cue_recall_fires == 0 on ALL seeds | true |
| C3 contact lift | ARM_CUE_ON P2 contact_rate > ARM_OFF per matched seed, >= 2/3 | **false** |
| C4 survival not regressed | ARM_CUE_ON P1 survival >= ARM_OFF (informational) | true |
| overall_pass | C1 AND C2 AND C3 | **false** |

Key arrays: `on_cue_fires = [0, 0, 0]` (zero fires across all three ON seeds);
`on_contact_rates = [0.0, 0.0, 0.335]`; `off_contact_rates = [0.0, 0.392, 0.659]`.

**Failed criterion: C1 -- an absolute / precondition criterion.** The ON arm never produced
the cue-recall event at all, so the load-bearing discrimination criterion (C3 contact lift)
was structurally untestable. "Negative control (C2) passes, precondition (C1) fails" is the
instrumentation / substrate-not-ready fingerprint -- NOT the substrate-ceiling fingerprint
(which is "negative control passes, discrimination fails *after the phenomenon was produced*").

## 2. Claim-layer mapping

`claim_ids = []`. This is a substrate-readiness diagnostic; no claim was placed under test,
so there is no falsification risk. SD-057 (object-bound incentive-salience; L6 cue-recall
MECH-347 / L7 dACC readout MECH-348, landed 2026-06-04) is **unaffected** -- the bridge never
got to express itself, so the run carries zero evidential weight for or against it.

## 3. Biological-reference triage

- **Closest mechanism:** Berridge incentive-salience ("wanting") -- a perceived-but-uncontacted
  object acquiring a dopaminergic approach spur via a stored incentive value.
- **Dependencies in real brains:** the incentive token must be *formed* before it can be
  *recalled*. Biologically, early value is seeded by provisioning / parental feeding (the
  nursery stage), not by the animal's own foraging contact.
- **Is formal import?** No -- this is a faithful biological translation, not a Pearl/Shannon
  formal import. The biology is already grounded; no lit-pull is owed.
- **Missing-dependency signature?** Yes. The failure is exactly what happens if the
  formation stage is absent: the bank can only bind a token on real typed contact, but the
  cue was meant to *bootstrap* contact -- chicken-and-egg. Stage-0 forced feed (the nursery
  analog) was decoupled from typed contact (`rt = _contacted_resource_type(obs)` ~always None),
  so it never seeded the token. This is a discovered/repaired prerequisite, not a falsification.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|-------|--------|-------|
| Claim alignment | intact | no claim tagged; SD-057 bridge never expressed |
| Biological reference | clear | Berridge wanting; nursery-seeded token; failure = missing-formation-stage signature |
| Prerequisites | missing | Stage-0 incentive-token formation absent -> bank empty entering P1/P2 |
| Implementation | partial / stub | bridge wired but token never bound (symbol of mechanism, not functional role); bare `except: pass` masked the zero |
| Environment | adequate | scaffold envs SD-049-enabled; 634c seeding regime present |
| Measurement | under-instrumented / misleading | C1 read `getattr(p2,'n_cue_recall_fires',0)` = 0 (no such aggregate); no cue_diag attribution |
| Integration | partially coupled | formation stage decoupled from recall stage |
| Scale / capacity | adequate | -- |

**Recommended epistemic_category:** `substrate_not_ready` (instrumentation + formation gap).
Explicitly NOT `substrate_ceiling`.

## 5. Learning extracted

1. **Chicken-and-egg formation gap.** `IncentiveTokenBank` only binds on real typed contact,
   but cue-recall was meant to bootstrap contact -> bank empty -> `cue_recall_wanting` returns 0
   at `k not in bank._base_value` -> `cue_fires=0`. Fixed by `scaffold_stage0_bind_incentive_token`
   (binds the strongest-perceived type at Stage-0; shared `_strongest_perceived_type` helper so
   formation and recall use identical perception). Bit-identical OFF.
2. **Silent-failure anti-pattern.** A bare `except: pass` in `_maybe_cue_recall` made the zero
   undiagnosable. Replaced with a `cue_diag` accumulator attributing every non-fire to a reason
   (no_token / resource_field_absent / proximity / amp_zero / exception:<Type>) plus substrate
   quantities (token_bank_size, drive_peak, attempts/matches/fires). Surfaced on P1/P2 results
   + Stage0.token_bank_size_end.
3. **Measurement bug.** C1 read a non-existent aggregate field (always 0 even when the cue
   fires). 638a sources cue fires from `cue_diag['n_cue_recall_fires']`; `636128a` adds the
   aggregate to P1/P2 results.

## 6. Repair pathway (routing)

**Routing: `queue-experiment` -- already executed.**

- Fix landed: `a9ef0be` (token-formation + instrumentation), `636128a` (n_cue_recall_fires aggregation).
- Validation re-issue: **V3-EXQ-638a** queued (`0258238`), running on ree-cloud-2. 638a does NOT
  supersede 638 -- 638's cue-silent evidence is the valid failure record 638a fixes.
- **No new substrate_queue entry** (`recommended_substrate_queue_entry.action = "none"`): the fix
  is harness-level code that has landed; SD-057 substrate is untouched.
- **No demotion** (no claim tagged). **No lit-pull** (biology already grounded).

638a interpretation grid (carried for governance):
- C1 + C3 PASS -> formation gap was the whole story.
- C1 PASS + C3 FAIL -> cue fires without authority -> interoceptive need-gating layer + 638b
  (drive_peak ~0.04 in smoke = the layer-2 signal).
- C1 FAIL -> re-audit via `cue_nonfire_reason_counts` (now diagnosable).

## 7. Recommended evidence_quality_note (for governance to write on the 638 record)

> V3-EXQ-638 (diagnostic, no claims) was cue-silent: C1 false, `on_cue_fires=[0,0,0]`. Root cause
> (code-confirmed): the IncentiveTokenBank was empty entering P1/P2 because Stage-0 forced feed was
> decoupled from typed contact, so no incentive token ever bound -- the cue-recall bridge could not
> bootstrap the very contact needed to form its token (chicken-and-egg), compounded by an
> `except: pass` that hid the zero and a C1 metric that read a non-existent aggregate. Instrumentation
> + formation gap (`substrate_not_ready`), not a claim or substrate-ceiling result. Fixed at the
> harness layer (`a9ef0be` + `636128a`); validated by V3-EXQ-638a (running). non_contributory for
> governance weighting; contributory as a substrate-readiness finding.
