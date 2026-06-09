Raw thought file: [docs/thoughts/2026-06-06_ca3_development_sparse_structured_connectivity.md](../../docs/thoughts/2026-06-06_ca3_development_sparse_structured_connectivity.md)
Intake date: 2026-06-09
Status: structured intake (Stage 2)
Classification: developmental architecture compass -- NOT a REE-v3 implementation target
Registration: NONE (no claims.yaml entry; candidate claims below are FOR FUTURE REGISTRATION only)

---

# THOUGHT INTAKE (Stage 2): CA3 development from dense/random to sparse/structured memory circuitry

## 0. Source verification (resolves the raw note's "partial" status)

The raw thought recorded the primary source as **unverified** (the `share.google` link
was not opened and the Nature Communications page was not located during capture). This
intake **verifies the primary source**:

- **Primary (VERIFIED):** Vargas-Barroso V., Watson J. F., Navas-Olive A., Schlogl A., Jonas P.
  "Developmental emergence of sparse and structured synaptic connectivity in the hippocampal
  CA3 memory circuit." *Nature Communications* (2026). DOI article
  `s41467-026-71914-x`. https://www.nature.com/articles/s41467-026-71914-x
- **Institution:** Institute of Science and Technology Austria (ISTA). The raw note's
  attribution to Peter Jonas + Victor Vargas-Barroso is **confirmed**; full author list adds
  Watson, Navas-Olive, Schlogl.

**Findings as reported in the primary abstract + ISTA/EurekAlert coverage (verified):**

- Multicellular patch-clamp circuit mapping of up to **8 CA3 pyramidal neurons** simultaneously,
  at three postnatal stages: **P7-8 (early), P18-25 (adolescent), P45-50 (adult)**.
- CA3 recurrent connectivity transforms from **local, dense, strong, and (near-)random** ->
  **distributed, sparse, and structured**.
- **Early:** a *single* synaptic event can be sufficient to trigger a postsynaptic spike.
- **Mature:** **spatial summation of several (weaker) inputs** is required to drive a spike.
- Authors frame this as **"tabula plena"** (a full, over-connected starting substrate that is
  *refined by pruning*) rather than tabula rasa, and suggest the sparse/structured endpoint may
  emerge via **experience-dependent** mechanisms.

**What could NOT be independently re-verified at intake:** the precise quantitative connection
probabilities / EPSP amplitudes per stage (behind the article; abstract-level only). Not needed
for a developmental compass; flag for the future architecture-note author if quantitative anchors
are wanted.

**Corroborating secondary source (independent, human CA3):** Tang et al., "Human hippocampal CA3
uses specific functional connectivity rules for efficient associative memory," *Cell* (2024) --
mature CA3 is *structured*, not random, which is the endpoint of the developmental trajectory
above. Useful as a cross-species "the mature state is structured" anchor; does NOT speak to the
developmental pruning dynamics.

---

## 1. Verbatim thought (preserved)

> A saved REE email pointed to a Nature Communications article titled "Developmental emergence of
> sparse and structured synaptic connectivity in the hippocampal CA3 memory circuit". [...]
> The reported pattern is: immature CA3 begins with dense, strong, relatively random connectivity;
> development reduces/prunes connections; mature CA3 becomes sparser and more structured;
> individual immature synapses may be strong enough to trigger spikes; mature neurons require
> coordinated activation from multiple weaker inputs.
>
> The useful REE idea is:
>
> > a memory circuit may not develop by adding connectivity to an empty substrate, but by pruning
> > an overconnected substrate into sparse, structured, cooperative computation.
>
> For REE, this supports a developmental principle: early cognifold construction may require
> overconnected exploratory coupling followed by pruning, sparsification, and structured gating
> rather than starting from clean modular sparsity.

(Full original text retained in the raw thought file; sections 2-9 there carry the proposed
classification, REE-architecture mapping table, the `mature_recall_activation` formulation,
the failure-mode mapping, cautions, external anchors, the proposed `developmental_pruning_and_
sparse_memory_cognifold.md` note, and the guardrail for future agents.)

---

## 2. What's New vs Existing REE Docs (novelty table)

| Idea in this thought | Already covered in REE? | Where | Genuinely new? |
|---|---|---|---|
| Mature memory circuitry is **sparse + structured** | YES (as an endpoint/property) | ARC-006 "Entities are sparse, persistent, bindable structures"; ARC-007 hippocampal map | NO -- the *endpoint* is already asserted |
| Sparse structure arises by **pruning an over-connected start** (subtractive, not additive) | **NO** -- REE developmental claims are *additive / curriculum-gated* | ARC-019 (staged curriculum), IMPL-019 (self-first ordering) describe adding capability in stages, not pruning an over-connected substrate | **YES** -- subtractive developmental mechanism is absent |
| "**Tabula plena**" -- start full/over-connected, refine down | **NO** explicit framing | -- | **YES** -- REE has no over-potential-field-then-prune principle |
| Down-scaling / homeostatic synaptic pruning during offline phases | PARTIAL (offline down-scaling exists) but framed as **denoising/SHY**, NOT as *developmental sparsification* | MECH-120 (SWS denoising / attractor flattening, Tononi SHY) -- V4 scope | **PARTIAL** -- mechanism analog exists; *developmental* reframing is new |
| Transition from **single-strong-cue authority** -> **convergent-weak-input (spatial summation) recall** | PARTIAL -- cue/representative-authority is an active V3 problem, but not framed developmentally | E3 candidate selection / cue-authority work (ARC-062/MECH-309 rule-apprehension lineage; SD-033a bias head); MECH-076 attractor lock-in | **YES** -- "immature single-cue dominance matures into convergent multi-cue recall" is a new diagnostic lens |
| Failure modes from *failure to mature* (confabulatory completion, belief fixation, precision misallocation, provenance collapse) | PARTIAL -- the failure modes exist as separate claims | MECH-094 (provenance/hypothesis tag -> confabulation), MECH-076 (attractor lock-in -> OCD/belief fixation) | **PARTIAL** -- the *developmental-immaturity* common cause is the new framing |
| Maturation of memory circuits **before full action authority** ("developmental gates before a trace can influence action release") | PARTIAL -- gating-before-action exists (commitment/BetaGate), not as a developmental maturity gate | ARC-028 / MECH-090 commitment gate; MECH-022 control-plane-gated hypothesis injection | **PARTIAL** -- developmental readiness-gate-on-memory is new |

**Net novelty:** the durable new idea is **subtractive ("tabula plena" -> pruning) developmental
sparsification** as a possible route to the sparse/structured endpoint REE already asserts -- plus
its corollary that **mature recall is convergent-weak-input, not single-strong-cue**. Everything
else is a reframing of existing claims through a developmental lens.

---

## 3. Key formulations

**(a) Tabula plena, not tabula rasa.** Construction may proceed from an over-connected exploratory
field refined *down* by pruning/down-weighting/gating, rather than from an empty modular skeleton
filled *up*.

**(b) Mature recall = convergent weak inputs, not max single cue.** From the raw thought:

```
mature_recall_activation = f(convergent_weak_inputs, context_match, residue_state,
                             goal_state, self_world_tag, precision_gate)
```
rather than
```
mature_recall_activation = max(single_strong_cue)
```

**(c) Three-phase developmental schedule (hypothesis):**
1. Over-connected exploratory phase -- many weakly-constrained associations, high plasticity,
   broad coupling, **low action authority**.
2. Pruning / selection phase -- repeated offline + waking experience down-weights unstable /
   non-useful pathways.
3. Sparse structured retrieval phase -- mature recall requires coordinated multi-cue activation.

**(d) Pruning is not (only) deletion.** Down-weighting, gating, or contextualisation are likely
better computational analogues than hard edge-deletion (raw-thought caution, retained).

---

## 4. Affected existing claims (REAL ids -- verified against claims.yaml 2026-06-09)

These are claims the idea *touches*. **No edits made to any of them.** This is a compass note.

| Claim | What it is | Relation to this thought |
|---|---|---|
| **ARC-006** | "Entities are sparse, persistent, bindable structures." | States the sparse endpoint; says nothing about how sparsity is *reached*. Subtractive-development would be a mechanism story under it. |
| **ARC-007** | Hippocampal systems store/replay paths through residue-field terrain (cognitive map substrate). | The CA3 recurrent circuit is the biological locus; mature structured connectivity is what makes path/relational memory reliable. |
| **ARC-019** | REE requires staged developmental training with explicit curriculum gates. | Closest existing home. Currently **additive** (add capability per stage). This thought proposes adding a **subtractive/pruning** stage -- a candidate amendment, not a contradiction. |
| **IMPL-019** | Self-first, social-later developmental ordering heuristic. | Same developmental-ordering family; orthogonal axis (what-order vs add-vs-prune). |
| **MECH-120** | SWS denoising / attractor flattening (Tononi SHY synaptic homeostasis). **V4 scope.** | The existing mechanism analog closest to "pruning / down-scaling." Reframing SHY as *developmental sparsification* (not just nightly denoising) is the overlap. |
| **MECH-094** | Hypothesis / provenance tagging (tag-loss -> confabulation). | Failure-mode link: "provenance collapse / confabulatory completion" from un-pruned over-connected completion. |
| **MECH-076** | Attractor lock-in (OCD analog; abnormally deep basin). | Failure-mode link: "belief fixation = early strong attractor survives without pruning." |
| **MECH-022** | Hippocampal hypothesis injection gated by control plane. | Relates to "maturation before action authority" (gating a trace before it influences release). |
| **ARC-028 / MECH-090** | Commitment / BetaGate (trajectory candidacy before action). | The existing action-readiness gate; a developmental-maturity gate would be a distinct, higher-level conditioning of it. |

**Adjacent but DEFERRED (do not pull onto this):** the play-mode cluster (ARC-049/050 + MECH-194..199,
INV-058/059/060) is the natural home for an "exploratory over-connected phase," but per the
play-mode memo it is **entirely substrate-blocked in V3** (no `play_frame_tag`, no synthetic-signal
seeding) -- a probe there self-routes `blocked_substrate`. Note the linkage; do not queue against it.

---

## 5. Candidate claims FOR FUTURE REGISTRATION (NOT registered here)

Recorded so a later session can register if/when this leaves the compass stage. **None of these
are in claims.yaml. Do not register from this intake.**

- **Candidate MECH (subtractive developmental sparsification):** "Mature sparse/structured memory
  connectivity emerges by pruning / down-weighting an initially over-connected (`tabula plena`)
  substrate, not by additively growing connections onto a sparse skeleton." -- mechanism_hypothesis;
  `implementation_phase: v4` (consolidation/SHY-adjacent); `emergent_from` would include MECH-120.
  Likely **amends ARC-019** rather than standing fully alone.
- **Candidate MECH (convergent-weak-input recall vs single-strong-cue):** "Mature recall requires
  spatial summation of multiple weak, context-convergent cues; single-strong-cue dominance is an
  immature regime to be outgrown." -- ties to the cue-authority / representative-authority problem
  (ARC-062/MECH-309 lineage; SD-033a bias head). This is the **most V3-relevant** strand because
  REE-v3 *currently* exhibits single-cue/single-representative over-authority (the active
  rule-apprehension and behavioural-diversity work). Could be framed as a diagnostic lens on
  existing claims rather than a new claim.
- **Candidate Q (open question):** "Should REE distinguish an early over-connected exploratory
  developmental substrate from a mature sparse/structured substrate -- and is pruning best modelled
  as deletion, down-weighting, gating, or residue-tagged de-authorization?" -- answer_state /
  open_question.
- **Candidate ARC-note (not a claim yet):** the raw thought's proposed
  `docs/architecture/developmental_pruning_and_sparse_memory_cognifold.md`.

Registration gating note: this is a **V4-leaning developmental compass off the V3 critical path**.
The V3-relevant *fork* is the convergent-weak-input-vs-single-strong-cue lens, which should be
folded into the *existing* cue-authority / rule-apprehension work rather than opening a new line.

---

## 6. Relevance to REE failure modes (from raw thought, mapped to real claims)

| Failure pattern (raw thought) | REE claim it maps to |
|---|---|
| confabulatory completion (over-connected pattern completion, insufficient structure) | MECH-094 (tag/provenance loss -> confabulation) |
| belief fixation (early strong attractor survives un-pruned) | MECH-076 (attractor lock-in) |
| precision misallocation (single cue gets excessive authority) | cue-authority / SD-033a bias-head; precision-gating cluster |
| goal proxy lock-in (early association over-authoritative) | goal-pipeline / proxy-reward work |
| provenance collapse (traces bind without structured source tagging) | MECH-094 |

This is a *unifying-cause* hypothesis (failure-to-mature-from-dense-to-sparse), not new failure
modes. Useful for the `ai-cognitive-failure-taxonomy` later; immediate home is REE_assembly because
the primary issue is developmental memory architecture.

---

## 7. Cautions (carried forward verbatim intent)

- Do NOT overgeneralise mouse CA3 development to human cognition or REE design.
- Do NOT treat dense early connectivity as automatically good/bad.
- Do NOT assume pruning = deletion only (down-weighting / gating / contextualisation may be better).
- Do NOT make this a REE-v3 implementation target without a specific existing substrate gap.
- **Guardrail (from raw section 9):** if a future agent tries to convert this into "add more
  connections" or "delete weak connections," STOP and reframe. Correct near-term extraction:
  *preserve developmental pruning/sparsification as a possible route from over-connected exploratory
  memory to mature structured recall.*

---

## 8. Next steps (none on the V3 critical path)

1. **(Optional, if elevated)** Quantitative source pass: pull the per-stage connection-probability
   / EPSP-summation numbers from the Nature Comms article to anchor any future architecture note.
2. **(DONE 2026-06-09, V3-relevant)** The **convergent-weak-input vs single-strong-cue** lens was
   folded into the selection-authority work as a durable cross-reference: see the "Developmental
   framing (compass)" block in
   [modulatory_bias_selection_authority_design.md](modulatory_bias_selection_authority_design.md)
   Related Work. It is a diagnostic lens for tuning `modulatory_authority_gain`, NOT a new claim
   line (none opened).
3. **(Deferred, V4)** If/when MECH-120 (SHY) or the play-mode exploratory substrate is built,
   revisit whether a *developmental* subtractive-sparsification stage should amend ARC-019.
4. **(Compass)** Leave the raw thought's proposed
   `developmental_pruning_and_sparse_memory_cognifold.md` architecture note as a *future* artifact;
   do not write it now -- the idea is not yet on a closure path.

No claims.yaml registration, no substrate, no queued experiment from this intake.

---

## 9. External anchors

- **Primary (verified):** Vargas-Barroso, Watson, Navas-Olive, Schlogl, Jonas. *Nature Communications*
  2026. https://www.nature.com/articles/s41467-026-71914-x
- **ISTA / coverage:** EurekAlert "Do memories form on a blank slate?"; Neuroscience News
  "Why the Brain Starts with 'Too Much' to Build Memories" (tabula plena framing).
- **Corroborating mature-CA3-is-structured (cross-species):** Tang et al., *Cell* 2024,
  "Human hippocampal CA3 uses specific functional connectivity rules for efficient associative memory."
- **Source email:** Daniel Golden saved the Nature-linked item 2026-05-11.
