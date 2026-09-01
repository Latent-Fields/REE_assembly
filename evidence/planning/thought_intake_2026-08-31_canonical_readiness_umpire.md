# Thought Intake: Canonical Readiness Umpire — detecting when a reference organism has emerged

- **Date processed:** 2026-09-01
- **Raw thought:** `docs/thoughts/2026-08-31_canonical_readiness_umpire.md`
- **Session:** planning-metabolise-20260901

## Verbatim core proposal

"The system should be able to recognise when the evidence warrants asking whether a canonical organism has emerged, while remaining structurally unable to answer that question by itself." An umpire, not a ruler: state machine (NO_WARRANT / ADMISSION_PASS_WARRANTED / REFERENCE_ORGANISM_REVIEW_WARRANTED / USER_DECISION_REQUIRED / CANONICAL_OBSERVED), gates not a score (Gate A identifiable organism, B admission-doctrine candidate substrate, C **coexistence** — "mechanisms demonstrated in different experimental animals do not compose into a competent organism merely because they share a repository", D whole-organism non-degeneracy, E behavioural evidence, F reproducibility — with the developmental identity note: the reproducible object may be the developmental recipe and constitution, not the adult state). Structural prohibition on self-canonisation; escalate transitions, not persistent states (Steward principle); warrants are withdrawable; profile-admission readiness and reference-organism readiness deliberately separate thresholds. Expected immediate V3 output: NO_WARRANT, with reasons. Full-lineage principle, first implementation around V3 as derived artifacts (`canonical_readiness.v1.json` + `.md`).

## What's new vs. existing REE docs/claims

| Thread | Existing coverage | Verdict |
|---|---|---|
| Canonical-profile mechanism | ree-v3 `ree_core/utils/canonical_profile.py` (mechanism exists, `_PROFILES` deliberately empty; admission criteria = architecture_epoch_investigation.md sections 7-9, governance-gated) | Already-built MECHANISM; the umpire is its missing front door — cross-ref only |
| Capability/plasticity preflight | **GOV-CAPCONTRACT-1** (organism must be able to express/acquire the faculty; "did not learn" != "could not have learned") — Gate D/E lean on it directly | Already-owned; depends_on |
| Escalate-transitions-only | Steward architecture (escalate new info only) | Existing principle, reused |
| Readiness DETECTION as a governance function with no canonical authority; coexistence gate; two-threshold separation; withdrawable warrants | Nothing — no machinery notices "it is now time to ask"; the experiment-specific-REEs problem is an interpretive caveat only | **Genuinely new — registered below** |

## Key formulations

> "Canonical readiness is a set of gates, not a progress percentage."
> "The first important transition is not 'the architecture is finished,' but 'essentially the same animal keeps reappearing and surviving broader tests.'"
> "The umpire may call for adjudication. It may never adjudicate its own call."

## Candidate claims — REGISTERED this pass

- **GOV-UMPIRE-1** — canonical readiness umpire (lineage-level governance rule): REE maintains an explicit, inspectable, authority-free process for recognising when reference-organism review is warranted; the detector derives/report/escalates and structurally cannot canonise.

## Next steps

1. Engineering follow-on (campaign candidate): deterministic detector deriving `canonical_readiness.v1.json` + human-readable report from experimental manifests (fingerprint coexistence analysis is the substantive new computation — Gate C). Conservative posture: unknown/false/unmeasured stay distinct; missing instrumentation must not read as green.
2. Integrates with /governance cycles once built; escalate transitions only.
3. Not registered as separate claims: the individual gates (they are the detector's design, owned by GOV-UMPIRE-1's implementation doc when written).
