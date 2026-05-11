# SYNTHESIS — Q-045 LC-NE noise-floor vs dACC anti-recency substrate independence

**Pull date:** 2026-05-11. **Entries:** 5 papers — Tervo 2014 (Cell), Scholl 2015 (J Neurosci), Meder 2017 (Nat Commun), Yu & Dayan 2005 (Neuron), Kennerley 2006 (Nat Neurosci).
**Anchor claim:** Q-045 — Is MECH-313 (LC-NE tonic noise floor) a separate parameter from MECH-260 (dACC anti-recency penalty), or do they collapse into one anti-monostrategy substrate?
**Source attribution:** the per-paper records cite PubMed and include DOI links; this synthesis aggregates and adjudicates rather than re-citing each paper exhaustively.

---

## Why this pull

Q-045 was registered 2026-05-10 as an open question from the ARC-065 Pull 1 R3 verdict ("relationship between LC-NE noise and dACC anti-recency is architecturally distinct but functionally overlapping; needs empirical resolution"). The Q-045 resolution plan is a 4-arm ablation on the SD-054 reef substrate with ARC-062 gated-policy enabled: both-OFF / 313-only / 260-only / both-ON, with behavioural-diversity ranking determining whether the two mechanisms are mutually load-bearing or one dominates. At registration, Q-045 had 0 experimental and 0 literature entries. The ARC-065 Pull 1 synthesis also flagged a separate hygiene gap: the MECH-260 anchor (Scholl 2015) was not retrievable in that pull and needed re-extraction. This automated PM lit-pull addresses both gaps in a single 5-paper review.

## R1 — Substrate coupling: do LC-NE and dACC act independently on behavioural variability?

**Verdict: NO, COUPLED-NOT-COLLAPSED.** Tervo et al. 2014 (Cell) is the load-bearing empirical paper. Using transgenic LC-cre rats with viral targeting of the LC -> ACC projection, they show that the strategic-vs-stochastic behavioural-mode switch in rats playing a virtual competitor is gated by LC-NE input INTO ACC. During stochastic mode, normal ACC engagement (its history-tracking output) is SUPPRESSED. LC-NE upstream, ACC downstream, directional gating. This is incompatible with the simplest version of Q-045 (parallel orthogonal substrates) and also incompatible with the simplest collapse (single regulator with two flavours). The correct architectural framing is COUPLED-NOT-COLLAPSED: MECH-313 (LC-tonic-noise substrate) and MECH-260 (dACC anti-recency substrate) are substrate-distinct, but MECH-313 should be wired to gate MECH-260's contribution rather than run beside it on a fully parallel pathway. Tervo's mode-switch is discrete (state-switch) where MECH-313 is conceived as continuous (always-on noise floor); the architectural mapping is at the directional-coupling level, not the dynamic level.

## R2 — Substrate distinctness: does dACC do something computationally specific that a noise-floor cannot reproduce?

**Verdict: YES, CONFIRMED.** Scholl et al. 2015 (J Neurosci) — the MECH-260 anchor paper recovered by this pull, having been flagged as un-retrievable in the ARC-065 Pull 1 synthesis — shows that dACC, frontal operculum / anterior insula, and lateral anterior prefrontal cortex SELECTIVELY SUPPRESS irrelevant reward influences on choice. Their data are content-conditional: the same reward magnitude with a different label (real vs hypothetical) produces different anti-recency responses. A noise-floor primitive (MECH-313's class) is content-uniform by construction — it perturbs all features equally. A content-selective anti-recency gate (MECH-260's class) is a computationally distinct primitive that adds information the system did not previously have. Kennerley et al. 2006 (Nat Neurosci) supplies the causal leg: ACC lesion in macaques produces a selective impairment in action-outcome history integration (preserved within-trial error-detection; impaired across-trial sustained-rewarded-response and risk-payoff integration). dACC is necessary for history-integration in general; Scholl 2015 narrows this to content-selective anti-recency specifically. The two anchors together establish that MECH-260's substrate is doing something computationally elaborate that MECH-313's noise primitive cannot reproduce.

Meder et al. 2017 (Nat Commun) reinforces this from a third angle: dACC holds a multi-timescale value spectrum, organised as a cortical gradient, dynamically rebalanced as the environment changes. The shorter-timescale value representations are the ones anti-recency suppression would operate on. This is structurally incompatible with a uniform noise-floor primitive.

## R3 — Computational distinctness from theoretical first principles

**Verdict: SUPPORTING.** Yu & Dayan 2005 (Neuron) provides the canonical Bayesian-theoretic version of the substrate-distinctness argument. NE signals UNEXPECTED uncertainty (context-switch detection, drive belief-revision); ACh signals EXPECTED uncertainty (known cue unreliability); dACC sits downstream of both and computes value from history. These are computationally distinct primitives with different temporal kernels, different update rules, different gating conditions. Collapsing NE-substrate and dACC-substrate into one regulator would lose one of the two computational roles. This is theoretical-only support and shares some looseness in mapping: Yu-Dayan's NE role is unexpected-uncertainty signalling (triggered) while MECH-313 is currently a tonic-noise-floor (always-on). The arc_065 synthesis already noted this — MECH-104 covers the phasic / unexpected-uncertainty role; MECH-313 covers the tonic role. Yu-Dayan adds that the tonic role MAY need an unexpected-uncertainty modulation on its amplitude (a state-switch on top of the always-on baseline). This is a Phase-2 architectural refinement, not a current substrate gap.

## R4 — Predictions for the 4-arm ablation

The Q-045 resolution plan is a 4-arm ablation on SD-054 with ARC-062 gated-policy enabled: both-OFF / 313-only / 260-only / both-ON. The Q-045 notes propose three outcome categories: mutually load-bearing (both promote to provisional), 313-dominant (consider retiring MECH-260), 260-dominant (consider not implementing MECH-313 in V3). This pull's findings refine and constrain the predictions:

1. **both-OFF expected to show monomodal collapse.** This is the standing prediction from ARC-062 substrate-readiness diagnostics and is unchanged by this pull.

2. **313-only and 260-only should produce DISSOCIABLE behavioural signatures, not just different magnitudes of the same effect.** Per Scholl 2015 + Kennerley 2006, MECH-260's substrate does CONTENT-SELECTIVE history-integration; per Yu-Dayan 2005, MECH-313's substrate does CONTEXT-SWITCH-DETECTION (or in the simpler tonic version, baseline-noise). The behavioural signatures should differ in kind:
   - 313-only: should preserve within-trial sensitivity to immediate outcomes but show DIMINISHED behavioural-diversity GAIN OVER TIME as the agent commits to whatever option the noise floor happens to favour. Variability is uniformly distributed across choices and time.
   - 260-only: should show preserved action-outcome history learning (Kennerley) and content-selective bias suppression on choice (Scholl), but without an upstream trigger to enter the dissociative regime — the agent will continue to weight history-based predictions even when those predictions are unreliable.
   - If 313-only and 260-only produce INDISTINGUISHABLE diversity-with-discrimination patterns, this is evidence that MECH-260's V3 implementation has lost the content-selectivity that Scholl observed and is operating as noise. That would be a substrate failure, not a Q-045 collapse confirmation.

3. **both-ON should NOT be a linear superposition of 313-only and 260-only.** Per Tervo 2014, LC-NE dominance suppresses dACC engagement during stochastic mode. The expected pattern is: both-ON behaves more like 313-only than like a sum of the two singletons in the high-LC regime, and more like 260-only in the low-LC regime. The 4-arm ablation should ALSO measure under different MECH-313 amplitude settings to expose this asymmetry.

4. **R4 LOAD-BEARING refinement: 4-arm is INSUFFICIENT; needs to extend to 4-arm-x-2-LC-amplitude (8 cells).** The current Q-045 plan treats both-ON as a single condition. Tervo 2014 predicts directional-coupling-mediated asymmetry that the current plan cannot expose. The lit-pull's strongest pre-experiment refinement is to extend the 4-arm plan to test both-ON under low-LC and high-LC settings, or to include an additional ablation that selectively perturbs the LC -> ACC coupling itself.

## R5 — Substrate readiness for the 4-arm ablation

Kennerley 2006 raises a substrate-readiness concern that needs to be addressed before the 4-arm ablation runs. ACC's role in Kennerley's data is across-trial integration of action-outcome history — sustained-rewarded-response over many trials, risk-payoff integration in dynamic foraging. If SD-054 reef substrate as currently designed only generates short-horizon outcomes (a decision tick has its consequence within that tick or one downstream), the 4-arm ablation will not have the temporal-horizon to dissociate MECH-260 (across-trial history integration) from MECH-313 (within-tick noise floor) in the Kennerley sense. The substrate-readiness diagnostic for Q-045 should verify:

- SD-054 produces multi-trial outcome dependencies (at least 5-10 ticks before a choice's consequence fully resolves).
- The behavioural-diversity metric used for the 4-arm ranking captures BOTH within-tick choice variance AND across-trial commitment-pattern variance.
- The reef substrate supports a window long enough to observe the Kennerley-style sustained-rewarded-response phenotype that 260-OFF should impair.

If any of these are missing, the 4-arm ablation may produce a clean 313-dominance result that is an artefact of substrate insufficiency rather than a genuine architectural finding. This should be a precondition gate on Q-045 experiment authorisation, not a post-hoc caveat. The MECH-260 substrate-readiness diagnostic (analogue of V3-EXQ-544 for MECH-313) is the natural place to land this verification.

## Verdicts summary

| Verdict | Direction | Confidence | Implication |
|---|---|---|---|
| R1 LC-NE / dACC are substrate-coupled (not independent, not collapsed) | architectural | high | Keep MECH-313 + MECH-260 as separate sub-mechanisms; add directional coupling MECH-313 -> MECH-260 |
| R2 dACC substrate is computationally distinct from noise-floor primitive | empirical | high | Q-045 collapse hypothesis is REJECTED at substrate level |
| R3 NE and dACC have computationally distinct primitives | theoretical | moderate-high | Reinforces R2 from Bayesian-rational analysis |
| R4 4-arm ablation needs to be extended to expose LC-mediated asymmetry | design refinement | moderate | Extend to 8-cell design OR add LC -> ACC coupling ablation |
| R5 SD-054 substrate readiness for multi-trial outcome dependencies | substrate-gap diagnostic | moderate | Verify SD-054 temporal-horizon BEFORE 4-arm authorisation |

## What this pull DOES change

- Q-045 evidence_quality_note should be updated to record: substrate-coupling architecture (R1), substrate-distinctness verdict (R2/R3), 4-arm ablation refinements (R4), and substrate-readiness precondition (R5). The Q-045 outcome categories ("313 dominates", "260 dominates", "mutually load-bearing") should be expanded with a fourth category: "DIRECTIONALLY COUPLED" — the architectural verdict this pull surfaces.
- MECH-260 evidence_quality_note should be extended to cite Scholl 2015 + Kennerley 2006 as the substrate anchor pair (anchor-completion work flagged in arc_065 Pull 1 synthesis 2026-05-10).
- MECH-313 evidence_quality_note should be extended with a forward-looking note that the V3 substrate may need an unexpected-uncertainty trigger (Phase-2 refinement) if the 4-arm ablation surfaces under-specification.

## What this pull DOES NOT change

- No claims.yaml status changes. Q-045 remains `open`; MECH-313 remains `candidate_substrate_landed`; MECH-260 remains `substrate_landed` per ARC-065 Pull 1.
- No new claims registered. The R4 design refinement is a Q-045-internal refinement, not a new architectural claim.
- No new substrate work. The R5 substrate-readiness verification is a /queue-experiment task for a separate session, not a registration here.

## Aggregate lit_conf estimate

Five entries, mean source-quality 0.84, mean mapping-fidelity 0.77, mean transfer-risk 0.26. Indexer-derived `literature_confidence` for Q-045 expected to land in the 0.78-0.82 range, supports-direction-dominant (4 supports + 1 mixed). Evidence quadrant: plausible_unproven (high lit, no exp — expected since no V3 experiments queued against Q-045 yet).

## Open follow-ons

1. **Q-045 4-arm ablation design extension to expose Tervo asymmetry (R4)** — needs /queue-experiment session.
2. **SD-054 substrate-readiness verification for multi-trial outcome dependencies (R5)** — needs /queue-experiment session for substrate-readiness diagnostic.
3. **MECH-313 unexpected-uncertainty trigger refinement (R3)** — Phase-2 architectural question, conditional on 4-arm ablation result.
4. **MECH-260 multi-timescale value-spectrum refinement (Meder 2017)** — Phase-2 architectural question, conditional on 4-arm ablation result.

None of these block the current cluster of V3 work; they are surfaced here for future-session triage.
