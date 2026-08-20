# Failure autopsy -- V3-EXQ-937b (MECH-449 / ARC-107 per-bank envelope conversion joint)

- **Generated (UTC):** 2026-08-20T02:39:17Z
- **Scope:** single (diagnostic PASS -- autopsy mandatory by `experiment_purpose`, not by an adjudication flag)
- **Status:** confirmed (user gate 2026-08-20)
- **Session:** failure-autopsy-multi-20260819
- **Dry-run gate:** manifest checked, top-level `dry_run` absent -- not a smoke.

## 1. Why this PASS needed adjudicating

`experiment_purpose: diagnostic`, outcome PASS, `evidence_direction: supports` on
MECH-449 and ARC-107, all six criteria `passed: true`, and **no `adjudication`
flag** -- the case the 2026-08-07 rule change exists to catch. Two things made it
worth the read: the top-level `non_degenerate` field is **absent**, and the sole
load-bearing criterion measured exactly 1.0 on every seed.

## 2. The load-bearing criterion has exactly one reachable value

`C1_per_bank_envelope_conversion_lift`, threshold 0.4, measured
`{42: 1.0, 43: 1.0, 44: 1.0}` -- **zero variance across seeds, floors and K.**

Verified independently over the raw per-bank columns: **`converted == (pre_nogo_envelope_size >= 2)`
holds with 0 exceptions across all 12,672 ARM_CONSTITUTION banks.** Not "1.0 to six
decimal places" -- an identity.

The mechanism is analytic, not empirical:
1. The suppression vector is built to peak on the target (`:562`), exemplar
   `[0.0, 0.75, 0.125, 0.125]`, and `PERSEVERATION_FLOOR = 0.5`, so `soft_nogo` is
   always the singleton target.
2. For ARM_CONSTITUTION the target **is** the incumbent, i.e. the committed pick of
   the identical selector with the gate off (`:554`, `:561`).
3. `gng_protect_min_eligible = 1` (`e3_selector.py:1673-1690`): at envelope 1 the
   incumbent is re-admitted, so the pick cannot move (`converted = 0`, necessarily);
   at envelope >= 2 it is dropped and the argmin moves (`converted = 1`, necessarily).

Given both strata are populated -- which precondition P2 asserts -- C1's only
reachable value is 1.0. The 0.4 bar has **zero discriminating power**. The driver
says so in advance (`:230-232`): *"The mechanism predicts the per-bank lift is
1.0 - 0.0 = 1.0 against this 0.40 bar."*

The same argument forces C4 (0.0, the envelope==1 half of the identity), C5 (0.0 --
ARM_SHUFFLED suppresses a non-argmin, and removing a non-argmin cannot move the
argmin) and C6 (`protect_min` is K-independent, so "the step sits at 2" is entailed
at every K). C3 (0 empty-eligible sets) is the direct guarantee of
`gng_protect_min_eligible = 1` and can only fail if the guard itself is broken.

**None of the six is vacuous in the empty-set sense** -- every stratum holds
hundreds to thousands of banks. They are the stronger problem: **analytically
entailed**. This is a manipulation check, not a measurement.

## 3. The caveat's own instrument is tautological

The manifest's `construction_caveat` concedes the coupling is *"PARTLY A
CONSTRUCTION PROPERTY"* and says the run *"RECORDS that coupling per bank
(`per_bank.incumbent_is_f_argmin`) rather than asserting it away."*

That column does not measure what its name says. As coded (`:566-568`) it is
`argmax(suppression) == target`, and `suppression` was constructed one line earlier
to peak at `target`. Verified: **`incumbent_is_f_argmin == 1` on 38,016 of 38,016
banks -- 100%, including all 12,672 ARM_SHUFFLED banks, whose entire design premise
is that `target != incumbent`.** If the column meant its name, ARM_SHUFFLED would
read ~1/k, not 1.0.

So the caveat is **carried but unquantified**, and the word "PARTLY" understates it:
measured, the coupling is total.

## 4. The absent `non_degenerate` is an inherited lineage defect

The driver computes the verdict (`:977-982`) but emits it **only on the False
branch** (`:1401-1406`) -- there is no `else`. A non-degenerate run emits nothing.
Reconstructed from the manifest's own recorded values, all four conjuncts hold, so
the correct declaration is `non_degenerate: true`; the per-criterion dict is present
at `interpretation.criteria_non_degenerate` with all six true.

Third consecutive occurrence: 937 (`:895`), 937a (`:1078`), 937b (`:1401`) all emit
only on False; 940 and 941 emit unconditionally via `_lib/precondition_gate.py`,
which has existed since 2026-07-19 -- a month before 937b was authored. 937b imports
no `_lib` gate module and hand-rolls the logic. Nothing declares the omission, so it
reads as unintentional. **`validate_recording.py` cannot see it** -- the field is
outside `ALWAYS_CORE_KEYS`, and the manifest passes clean under `--strict`.

This is a **recording gap, not a data gap**: every quantity in this artifact was
recomputed from the manifest without re-running anything. The one genuine exception
is `incumbent_is_f_argmin`, which is a *wrong* measurement rather than a missing one,
and whose correct version is not recoverable from this manifest.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment (MECH-449) | **intact, not advanced** | Exercises the real gate on the real selector, but confirms arithmetic. MECH-449's own bar is behavioural: *">=1 previously-gated downstream channel CONVERTS into committed action"*. |
| Claim alignment (ARC-107) | **peripheral co-tag** | Touches one axis of one of six declared constitution components; none of Go, hyperdirect hold, channel competition, permission gate or latch. Three `depends_on` (ARC-108, ARC-109, MECH-450) still MISSING PIECE. |
| Biological reference | partial | ARC107_GROUNDING_SYNTHESIS L2 (Kravitz 2010 D1/D2 opponency, Mink 1996, Maia & Frank 2011), with a self-declared LOAD-BEARING divergence: biology uses two populations acting on movement vigour, REE folds Go/No-Go into eligibility pressures over an abstract candidate set. **The specific quantity measured here -- `gng_protect_min_eligible = 1` -- has no biological anchor at all**; no cited source predicts a discrete cardinality threshold on an eligible set. |
| Prerequisites | present | |
| Implementation | complete | The substrate does exactly what MECH-449 specifies. |
| Environment | n/a | Selection-face synthetic probe, no training, no agent loop (`reuse_ineligible_reasons: selection_face_synthetic_no_training`). |
| Measurement | **misleading** | C1 has one reachable value; the caveat's instrument is tautological; `combination_rule` omits the `step_is_sharp` conjunct the routing actually requires. |
| Integration | isolated | By design. |
| Scale | adequate but non-replicating | "3 of 3 seeds clearing" is not three confirmations: the outcome is a deterministic function of the mediator, so seeds vary only the bank draw. |

## 6. What the run does discharge -- stated plainly

937b was routed by `failure_autopsy_V3-EXQ-937-937a-cluster_2026-08-18` to emit the
per-bank joint that 937a computed and discarded, and it does exactly that: every
criterion re-keyed to the per-bank mediator, the joint emitted three ways, 937a's
`elapsed_seconds: null` always-core gap closed, and ARM_OFF's tautology carried into
the manifest. Its `aggregation_warning` is exemplary. The methodological repair is
real. What it did not close is `non_degenerate` -- a recording gap of exactly the
class the autopsy was about, in the same lineage.

## 7. Routing -- CONFIRMED at the user gate (2026-08-20)

**`governance`**, per-claim, declining the stamped `supports` on both.

- **MECH-449 -> `non_contributory`.** The run confirms the constitution's
  **arithmetic**, which its own `generality_caveat` concedes (*"confirms the
  constitution's ARITHMETIC, not any behavioural competence ... PROMOTES NOTHING"*).
  A criterion with one reachable value cannot support a behavioural claim.
  `epistemic_category` stays `standard`. Status stays `provisional`.
- **ARC-107 -> `non_contributory`, recorded per-claim as PERIPHERAL.**
- **Binding note for governance:** ARC-107 carries an **OPEN `pending_user`
  `promote_to_provisional` recommendation** whose own listed options include *"Hold
  until one additional confirming run"*. **This run must NOT be cited as that
  confirming run.** It is diagnostic-purpose (so it moves no count -- `genuine_exp_count`
  stays 2 and `latest_run_id` stays `v3_exq_926a`), it is a manipulation check, and
  it touches one axis of one component.
- **Driver fixes owed** (route to whoever next touches this lineage):
  1. emit `non_degenerate` unconditionally, or adopt `_lib/precondition_gate.py`
     (fixes 937/937a/937b as a class);
  2. repair or delete `per_bank.incumbent_is_f_argmin` -- as written it cannot
     support the caveat that cites it;
  3. complete `combination_rule` to name the `step_is_sharp` conjunct;
  4. stamp `evidence_direction_note` -- `claims.yaml` already complains about its
     absence on both claims for the *predecessor* runs, and it is absent again.
- `recommended_substrate_queue_entry.action: none` -- the 937/937a cluster autopsy
  already established there is no substrate gap, verified by source read and a
  4,224-bank re-measurement.

## 8. Recurrence

Brake **does not fire**: MECH-449 ceiling hits 0, ARC-107 0. Granularity-debt
trigger does not fire on either (no target reads `weakened`; the reader's own
verdict is *"measurement or implementation debt, NOT granularity debt"*).

**Pattern worth naming even though nothing fires:** of the four confirmed-autopsy
MECH-449 targets, **three are measurement/recording defects** (699, 699b, the
937/937a cluster). 937b is the fourth measurement-repair run in this claim's short
history, and it shipped with a fresh recording gap. That is not granularity debt --
it is a claim whose readouts keep needing repair, which is worth surfacing to
governance as a pattern rather than as a trigger.

## 9. Learning extracted

1. **A criterion whose value is entailed by the shipped code is a manipulation
   check, not a measurement** -- however large its margin or however many seeds
   clear it. The tell is zero variance across every axis that was supposed to vary.
2. **A caveat is only as good as the instrument it cites.** Naming a column as the
   record of a construction coupling is worse than not naming one if the column is
   tautological, because it converts an honest limitation into an apparent
   measurement.
3. **Emit non-degeneracy on both branches.** A field emitted only when False is
   indistinguishable, downstream, from a field never computed -- and
   `validate_recording.py` cannot catch it.
4. **Seed replication of a deterministic function is not replication.**
