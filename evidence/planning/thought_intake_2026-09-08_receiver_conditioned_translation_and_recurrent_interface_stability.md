# Thought intake -- Receiver-conditioned translation and recurrent interface stability

**Date processed:** 2026-09-08
**Raw thought:** `docs/thoughts/2026-09-08_receiver_conditioned_translation_and_recurrent_interface_stability.md` (252 lines)
**Session:** thought-ingest-receiver-conditioned-20260908
**Parent (already ingested, not re-derived):** `evidence/planning/thought_intake_2026-09-07_mutual_legibility.md`
(ARC-139, MECH-537..540, INV-105) and `evidence/planning/mutual_legibility_work_program_20260907.md`.
**Sibling processed in the same session:** `thought_intake_2026-09-08_deriving_the_cognitive_contract.md` (ARC-142).

Landing note: `claims.yaml` was owned by two active Wave-6 sessions when this pass began
(`w6-s5a-closure-20260908`, `w6hk-k-registry-20260908`, the latter editing mutual-legibility citations).
The claim was opened with `--allow-overlap` because this pass only APPENDS two new entries and touches
none of the entries those sessions edit; the new claims' anchors were placed in a NEW doc
(`docs/architecture/receiver_conditioned_translation.md`) rather than the mutual-legibility doc precisely
to stay off the file the registry-bundle session holds. The commit delta was read afterwards to confirm
nothing foreign was swept.

## 1. Verbatim core proposal

> `translated content = T(sender state, receiver state, receiver position/context)`
> ... the relevant communication subspace itself may be conditional on the receiver's current state.

> **An interface can be statically useful yet recurrently unstable.**

> Mutual legibility may be relational rather than fixed: what a sender should expose can depend on the
> receiver's current state. But an interface that is useful once is not necessarily safe to use
> repeatedly. In a recurrent cognitive system, translation must be both content-specific and dynamically
> self-consistent over time.

## 2. Novelty table

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| Only selected sender dimensions are visible to a consumer (s.1.2) | **MECH-537** communication-subspace routing | **Already owned** -- MECH-547 sharpens it (subspace conditional on receiver state) |
| Bridge ladder; a high-capacity bridge that succeeds is evidence about the bridge (s.6) | **MECH-538** | **Already owned** -- MECH-547 inherits the warning and states the exposure-not-solving constraint |
| Pairing-specificity; correct/mismatched/zero/random controls (s.4 items 6-7) | **INV-105** rungs 5-7 + consequence (1) | **Already owned as an evidence standard**; the receiver-permutation control is the addition |
| Good one-step + degrading long-horizon; map-initial-vs-re-map-each-step separation (s.2, s.5) | **MECH-539** dynamic compatibility | **Adjacent-but-distinct**: MECH-539 is bridge-vs-native-dynamics incompatibility; the new failure is the bridge's own output re-entering as input, separable by the clean-base arm -> MECH-548 |
| E1's own multi-step rollout fidelity | **INV-088** | **Already owned**, different object (cross-ref only) |
| Sleep adjusts / stabilises the interface; S1-S4 post-sleep signatures (s.5) | **MECH-540** | **Adjacent**: all four signatures are STATIC; the closed-loop post-sleep metric is folded into MECH-548's sleep corollary, and a fifth "static gain / dynamic loss" signature is left for governance |
| State vs modulatory overlay; gated, gained coupling edge; runaway gain (s.3) | **ARC-084** typed signed coupling, **MECH-363** all-cooperative runaway, MECH-048 stability overlays | **Adjacent at a different level** -- cross-ref as labelled analogy, not evidence |
| Cognitive contract: relations recoverable at a boundary (sibling intake) | **ARC-142** | **Cross-ref**: receiver-conditioning is HOW a recoverable relation is expressed, not WHAT must be preserved |
| Matched-capacity control discipline (s.6) | **GOV-MATCHAUX-1** | **Already owned** for representation objectives; inherited by MECH-547's confirming signature |
| Receiver-conditioned, context-indexed translation with the exposure-not-solving constraint and the permutation discriminator (s.1, s.6) | none (`grep -i "receiver-condition\|receiver state"` -> 0) | **NEW -> MECH-547** |
| Recurrent interface stability as a separate property; off-manifold compounding vs semantic double-counting; cumulative vs clean-base; eighth ladder rung; closed-loop sleep metric (s.2, s.3, s.5) | none (`grep -i "recurrent.*stab\|off-manifold\|double-count"` -> 0) | **NEW -> MECH-548** |
| The seven-arm assay and its measures (s.4) | work programme ML-13 (bridge ladder), ML-14 (causal replacement), receiver-manifold guard already listed | **Instrument, not claim** -- recorded on the location doc as an ML-13/ML-14 extension; chipped |
| XKV / kvloom evidence status (s.7) | none | **Motivation only**; not verified; lit-pull owed |

### Where this sits against the sibling intake

The cognitive contract (ARC-142) says WHAT must remain recoverable across a boundary. This thought says
two things about the translation that carries it: the expression of a recoverable relation may be
receiver-indexed (MECH-547), and the translation must stay valid under its own repeated application
(MECH-548). Neither changes ARC-139's central claim; the thought says so explicitly.

## 3. Key formulations (verbatim)

- "**An interface can be statically useful yet recurrently unstable.**"
- "the relevant communication subspace itself may be conditional on the receiver's current state."
- "receiver-conditioning should determine **what part of already-present sender information is exposed and
  how it is expressed**, rather than allowing the bridge to solve the task independently."
- "`one-step utility > 0` while failing `repeated closed-loop stability`."
- "Even a small per-step off-manifold displacement can accumulate until the receiver is operating in a
  state regime the bridge was never trained to handle."
- "It may be safer to test translated information first as an overlay or gated read surface rather than
  as an irreversible rewrite of the receiver's core latent state."
- "A sleep-induced interface change that improves a static probe but destabilises the next waking
  trajectory would be a failure, not consolidation."
- "Receiver-conditioned translation is powerful enough to become dangerous as an explanation."
- "This upgrades the evidence from author-only demonstration toward **early independent replication**, not
  settled replication."

## 4. Affected existing claims

Cross-referenced via `depends_on` only. **No status, confidence, evidence record or field of any existing
claim was touched.** Two amendments are PROPOSED to `/governance` rather than applied:

1. **INV-105 eighth rung** ("recurrently stable"), raised as a governance flag on INV-105 at registration.
   Amending a registered invariant's ladder is a governance decision, not an ingestion edit.
2. **MECH-540 fifth signature** (S5: static probe improves, next waking trajectory destabilises -- a
   failure, not consolidation). Left in MECH-548's sleep corollary; governance may lift it into MECH-540.

## 5. Candidate claims -- REGISTERED this pass

Both `status: candidate`, `substrate_conditional`, `implementation_phase: v4`, `registered_utc: 2026-09-08`,
location `docs/architecture/receiver_conditioned_translation.md` (new stub, parent "Core Engines & Forward
Models", nav_order 18).

| ID | Type | One line |
|---|---|---|
| **MECH-547** | mechanism_hypothesis | Receiver-conditioned, context-indexed translation: T(A,B) exposes which part of present sender content, never solves the task; confirmed only if receiver-permutation destroys a matched-capacity gain. |
| **MECH-548** | mechanism_hypothesis | Recurrent interface stability as a separate property: off-manifold compounding vs double-counting; cumulative vs clean-base; eighth ladder rung; closed-loop post-sleep metric. |

## 6. Deliberately NOT registered

- **The assay** (seven arms, eight measures, five readings). An instrument; it lives on the location doc
  and belongs in the work programme (ML-13/ML-14), where it is chipped.
- **A receiver-conditioned bridge for REE.** The thought is explicit: "None of these implications
  currently justify adding a receiver-conditioned bridge to REE."
- **XKV / kvloom as evidence.** Company/author demonstration plus an exploratory independent replication;
  recorded as motivation only.

## 7. Governance, REE, and more (the user's steer, carried over from the sibling pass)

**Governance.** One flag raised (INV-105, eighth rung). One admissibility consequence recorded inside
MECH-547 rather than as a new GOV rule: a receiver-conditioned bridge result is admissible only with the
receiver-permutation control and a sender-only matched-capacity baseline, on top of INV-105's existing
controls. If governance prefers this as a standing rule, it is a one-line extension of INV-105's
consequence list (a third consequence), not a new claim.

**REE itself.** The clean-base / overlay corollary is a design constraint for any future bridge in
`ree_core`: translated content enters as a gated overlay with its own gain (ARC-084's edge vocabulary),
never as a rewrite of the receiver's core latent. This also names a substrate gap shared with the sibling
intake: nothing in REE today represents *confidence in a translation* or *whether content was already
transmitted*, which is exactly what mechanism (b) needs to detect double-counting.

**And more.** The recurrence property generalises beyond bridges: any REE component whose output feeds
back as its own input on the next tick (E1 rollout, replay -> consolidation -> replay) has the same
one-step-vs-closed-loop distinction, and ARC-092's "no schema update from a consolidation cycle becomes
input to the next cycle without a waking checkpoint" is the same clean-base principle already registered
at the imagination boundary. Noted as a convergence clue, not merged.

## 8. Next steps

1. **Lit-pull owed** before XKV (Liu et al. 2026) or kvloom is cited as support; kvloom's collapse finding
   needs replication before it is anything but an emerging finding.
2. **Version routing belongs to /governance.** Both claims default to v4; the diagnostic is v3-runnable
   only once the ML-13 bridge-ladder library exists.
3. **Hardening deferred** -- no `what_would_answer` drafted (/thought-digestion). MECH-548's clean-base
   separating arm is the obvious digestion target.
4. **Work-programme extension chipped**: add arms 3-5 (permutation, cumulative, clean-base) and the drift /
   gain / re-injection measures to ML-13/ML-14, with the recurrence assay sequenced after ML-20's waking
   metric shows range and stability.
