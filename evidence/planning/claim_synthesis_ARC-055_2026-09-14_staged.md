**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml.**

# Claim synthesis: ARC-055 conjunct granularity

- Chip: `chip-20260910-arc055-conjunct-granularity-split`
- Session: headless metaworker (`d9e39d41-82a9-495c-87b1-78184e6d5e3e`), 2026-09-14
- Skill: `/claim-synthesis`, Steps 1-6 only (Step 7 registration deliberately NOT performed --
  see "Why this stops here" below)
- Trigger: two 2026-09-10 lit pulls landed 5 new entries in
  `REE_assembly/evidence/literature/targeted_review_arc_055/` (7 total), and the 4 conjuncts
  ARC-055 joins with "and" now have sharply divergent evidential standing that one aggregate
  `literature_confidence: 0.777` hides.

## Why this stops here (no claims.yaml edit in this pass)

Two independent reasons, either one sufficient on its own:

1. `/claim-synthesis`'s own Step 7 requires a live per-child `AskUserQuestion` approval before
   any registration ("**Proposal-first, governance-touching. Nothing lands in `claims.yaml`
   without the user's explicit per-child approval... Not safe headless.**"). This session is a
   headless `claude -p` worker with no live user to approve against.
2. `docs/claims/claims.yaml` is currently claimed by a concurrent session
   (`metaworker-chip-20260910-gflag0246-exq900-flat-benefit-autopsy`, opened
   2026-09-14T12:05:37Z, not stale) for unrelated GFLAG-0246 work. `task_claim.py open`
   correctly refused arbitration in this session's favor.

So this document is the Step 6 deliverable -- the decomposition proposal -- staged for
whoever next holds an uncontended `claims.yaml` claim to review and apply per Step 7.

## STOP-CHECK results (run before starting)

1. ARC-055 status/phase in `claims.yaml`: `('candidate', 'v4')` -- matches expected, not
   already resolved.
2. No prior `claim_synthesis`/granularity artifact for ARC-055 existed under
   `evidence/planning/` before this one.
3. `task_claim.py check` on `claims.yaml` + `targeted_review_arc_055`: **exit 3, contended**
   (see above) -- this is why registration is deferred rather than performed.
4. `claim_evidence.v1.json` for ARC-055: `lit=7, exp=0, lit_conf=0.777` (brief said 0.778;
   0.777 is what's actually on disk -- rounding, not a discrepancy), `direction_counts`
   `supports=5, mixed=1, weakens=1`. Matches.

## The four conjuncts and their evidence

ARC-055's text joins, with "and": (a) V(t)/D_V must be **explicit** signals, not emergent
epiphenomena; (b) they must be **available to and influence E3 trajectory selection**; (c)
D_V specifically has **temporal depth over horizon H**; (d) they **influence E1 state
representation, E2 transition-model prediction, and learning-update prioritisation**.

| Entry | Direction / conf | (a) explicit | (b) E3 selection | (c) D_V/horizon depth | (d) E1/E2 learning |
|---|---|---|---|---|---|
| Masset 2020 (OFC, abstract multi-read confidence) | supports 0.76 | **strong** -- abstract, multiply-read signal (predictive, not causal) | weak/indirect (time-investment consumer, not within-trial selection) | none -- "D_V is simply not addressed" | supports (cross-trial strategy-update consumer) |
| Meyniel 2017 (confidence-weighted learning, fMRI) | supports 0.72 (learning-leg only) | strong for the learning instantiation (separately reportable, independently localised) | untouched -- "claim's harder half... untouched" | none | **strong** -- reliability estimate demonstrably sets learning-rate |
| Zajkowski 2017 (frontopolar cTBS, Horizon Task) | supports 0.72 | supports (selectively removable term) | **strong, causal** -- directed exploration abolished, random exploration/noise untouched | **only real datum** -- effect present at horizon 6, absent at horizon 1; still "cousins, not the same thing" as D_V | none |
| Tervo 2014 (LC->ACC circuit, model-validity gate) | supports 0.71 | **undermined for this mechanism** -- gating quantity inferred from behavioural regime, not measured; noise-injection alternative (Kane 2017) fits equally well | **strong, causal, closest construct match** to V(t)-as-world-model-fit, but binary MODE switch not graded re-ranking | none | none |
| Schwartenbeck 2015 (policy precision / alpha_A, fMRI) | supports 0.68 | **cannot adjudicate** -- precision is a posit of the fitted model, not measured | weak/correlational only; entry itself says causal weight is carried by Zajkowski/Tervo, not this one | task has temporal extent but "not deep in the sense ARC-055 means by D_V" | none |
| Lak 2014 (OFC inactivation, wagering) | **mixed 0.60** | supports, causally ("unusually strong") | **weakens** -- decision accuracy survived inactivation; "E3 leg... currently unsupported by anything in this directory" (as of that entry) | none (2AFC, degenerate trajectory space) | none |
| Fleming 2014 (anterior PFC lesion, domain-specific) | **weakens 0.64** | orthogonal -- bears on whether "the signal" is even one object | **weakens** (2nd dissociation, same indirect route as Lak) | none (same 2AFC scope limit) | none |

**Per-conjunct read:**
- **(a) explicitness:** reasonably supported in the decision-confidence literature (Masset,
  Lak's causal half, Meyniel), but the entry with the closest construct match to V(t)-as-
  world-model-fit (Tervo) explicitly leaves explicitness undetermined, with a stated live
  alternative (noise injection, Kane 2017) requiring no represented signal at all.
- **(b) E3 selection availability:** genuinely contested exactly as the brief states -- two
  causal supports (Zajkowski, Tervo) against two causal-adjacent dissociations (Lak,
  Fleming), plus one correlational entry (Schwartenbeck) that explicitly disclaims
  adjudicating power. A 50/50-ish split hidden inside a 0.777 aggregate.
- **(c) D_V temporal depth:** **unevidenced**, as the brief states. Zajkowski's horizon
  interaction is the only entry that touches it at all, and even that entry's own author
  calls it "suggestive... nobody here measured a depth-like verisimilitude quantity."
- **(d) E1/E2 learning-update influence:** **best-evidenced conjunct** (Meyniel strong,
  Masset partial), and the only conjunct with a clean, non-contested positive read.

## Two findings beyond what the brief anticipated

### Finding 1: conjuncts (b) and (c) substantially duplicate ARC-054, which already has a sharper formulation and its own evidence base

`ARC-054` ("E3 trajectory selection must optimise predicted temporal-depth verisimilitude
D_V over planning horizon H, **not instantaneous V(t) alone**") is not a neighbouring claim
-- it is *the same assertion*, stated more precisely, that ARC-055's conjuncts (b)+(c) are
trying to make. ARC-054's notes already formalise `J(pi) = sum_k gamma^k * V_hat_pi(t+k)`,
`kappa_commit`, and the horizon-H argument, and already carry their own contested-grounding
history (GFLAG-0242: Gillespie 2021 weakens the hippocampal-replay grounding at 0.72,
Champion 2022 supports the computational tractability of the horizon-discounted
formulation).

There is even a direct tension between the two claims as currently worded: ARC-054 argues
selection should use D_V **instead of** instantaneous V(t) ("optimising instantaneous V(t)
alone is insufficient"), while ARC-055's conjunct (b) as literally written asserts V(t) *and*
D_V must both be "available to and influence E3 selection." ARC-054's more precise
formulation should win; ARC-055 restating the weaker/looser version alongside it is exactly
the kind of redundancy that makes a shared aggregate number misleading.

**Practical upshot:** the Zajkowski/Tervo/Lak/Fleming selection-availability evidence belongs
substantively to ARC-054, not to a new ARC-055 child. It should be cross-linked there (a
`governance_flag.py raise --flag-type evidence_discrepancy` naming ARC-054 and the four
`targeted_review_arc_055` entries is the mechanical route -- left to whoever applies this,
since it also touches `claims.yaml`/flag registries under active contention right now).

### Finding 2: conjunct (c) is also already claimed by INV-068, so it needs no new home at all

`INV-068` ("Temporal depth D_V(t): system behaviour must depend on temporal persistence of
verisimilitude coupling") already formally defines D_V, its EMA formulation, and --
explicitly -- lists "hippocampal trajectory evaluation" and "action selection" among what it
grounds. Between INV-068 (definition + what D_V grounds) and ARC-054 (D_V drives E3
selection over horizon H, with its own evidence base), there is no independent work left for
ARC-055's conjunct (c) to do. It should be struck from ARC-055 rather than spun into a new
candidate claim -- there is nothing to test that ARC-054/INV-068 don't already own.

### The Masset/Fleming tension (addressed per the brief)

Masset 2020 (abstract, modality-general OFC signal feeding two behavioural consumers) and
Fleming 2014 (metacognitive accuracy *fractionating by domain* -- perception impaired,
memory spared, same patients) are genuinely unresolved against each other, and Fleming's own
entry says so explicitly rather than averaging it away. This bears on the WHOLE claim family,
not just the E3 leg: if confidence-like signals are computed and consumed locally per-domain
rather than as one architecture-wide quantity on a shared bus, then ARC-055 (in any form) is
asserting the wrong *shape* -- one global V(t) with four consumers -- independently of
whether any individual conjunct holds.

This is not fully orthogonal to REE's own design, however: ARC-055's own notes already
anticipate a staged implementation ending in "Stage 3 = level-specific phase-aware
hierarchical V" -- i.e., REE's own roadmap already moves toward a level-specific V, which is
structurally closer to Fleming's fractionation picture than to Masset's single global signal.
**Recommendation: do not resolve this tension by assertion.** Keep it as a standing,
explicitly-flagged open question attached to the narrowed ARC-055 (below), so a future
targeted lit-pull or governance review revisits it rather than it silently disappearing into
an averaged confidence number again.

## Recommendation: NARROW (not a 4-way SPLIT, not KEEP-as-is)

A mechanical 4-way split was considered and rejected: conjuncts (b) and (c) are not
undersupplied territory needing their own new claims -- they are already claimed, more
precisely, by ARC-054 and INV-068. Minting new ARC-055 children for them would create
duplicate-scope claims tracking the same evidence twice under two different confidence
numbers, which is a worse outcome than the current conjunction.

**Proposed disposition:**

1. **Narrow ARC-055 to conjuncts (a)+(d) combined** (explicitness + E1/E2/learning-update
   influence). These two are evidentially coupled -- Masset and Meyniel both support them
   together, and no entry in the pull treats them as separable questions -- and neither is
   already owned by a sibling claim.

   Proposed narrowed title (id, status, phase, depends_on unchanged):
   > "Verisimilitude signal explicitness: V(t) and D_V must be explicit signals (addressable
   > representations, not emergent epiphenomena) that influence E1 state representation, the
   > E2 transition model, and learning-update prioritisation."

   Proposed notes addendum (append, do not delete the existing staging note):
   > "NARROWED 2026-09-14 (claim-synthesis, chip-20260910-arc055-conjunct-granularity-split):
   > originally conjoined four assertions; conjuncts (b) E3-selection-availability and (c)
   > D_V-temporal-depth are struck as duplicative of ARC-054 (which already asserts D_V over
   > horizon H drives E3 selection, with its own contested-grounding history under
   > GFLAG-0242) and INV-068 (which already defines D_V and lists E3 selection among what it
   > grounds). The Zajkowski 2017 / Tervo 2014 / Lak 2014 / Fleming 2014 selection-leg
   > evidence in targeted_review_arc_055/ bears substantively on ARC-054, not here -- see
   > evidence/planning/claim_synthesis_ARC-055_2026-09-14_staged.md for the full mapping.
   > OPEN QUESTION, deliberately not resolved: Masset 2020 (abstract, modality-general
   > confidence signal, supports 0.76) and Fleming 2014 (domain-fractionated metacognition,
   > weakens 0.64) are in unresolved tension over whether V(t) is one architecture-wide
   > signal or several local ones; REE's own Stage-3 'level-specific phase-aware
   > hierarchical V' roadmap leans toward the fractionated picture. Revisit before promotion
   > past candidate."

2. **Re-run the evidence indexer after narrowing** (`--index-only`, targeted paths, per
   CLAUDE.md's narrow-edits-only rule) so `claim_evidence.v1.json` recomputes
   `literature_confidence` over only the entries that actually bear on the narrowed claim.
   Expect the aggregate to move -- the current 0.777 is diluted by the unevidenced (c)
   conjunct and the contested (b) conjunct pulling in both directions; a recompute limited to
   the (a)+(d)-bearing entries (Masset, Meyniel, Lak's explicitness half, Fleming's
   domain-question) should read cleaner, though the indexer has no per-conjunct filter today,
   so this may require manually re-tagging which entries are cited for the narrowed claim
   rather than relying on automatic recompute. Flag this as a possible indexer gap if it
   comes up -- do not build tooling for it in this pass.

3. **Raise a `governance_flag.py --flag-type evidence_discrepancy` on ARC-054** pointing at
   the four selection-leg entries (Zajkowski, Tervo, Lak, Fleming) in
   `targeted_review_arc_055/`, so `/governance` picks up that ARC-054's own evidence base is
   incomplete without them. Do not silently leave this as prose in this file only -- the flag
   is what actually surfaces it to a pipeline that revisits it.

4. **Do not register a new claim for conjunct (c).** It is a strike, not a split -- INV-068 +
   ARC-054 already own that territory.

## What the reviewer needs to do to apply this

Once an uncontended claim on `docs/claims/claims.yaml` is available:

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/task_claim.py open \
  --session-id <slug> --session-label "ARC-055 narrow (apply staged synthesis)" \
  --task "Apply claim_synthesis_ARC-055_2026-09-14_staged.md: narrow ARC-055, flag ARC-054" \
  --resources REE_assembly/docs/claims/claims.yaml REE_assembly/docs/assets/data/claims.json
```

Then: edit ARC-055's title + append the notes addendum above (re-read the insertion region
immediately before editing, per CLAUDE.md concurrency rules); run
`python scripts/build_claims_json.py`; raise the ARC-054 evidence-discrepancy flag; commit
pathspec-limited (`docs/claims/claims.yaml docs/assets/data/claims.json
evidence/planning/claim_synthesis_ARC-055_2026-09-14_staged.md`) via `ree_commit.py`; push.

## Sources

All 7 entries under `REE_assembly/evidence/literature/targeted_review_arc_055/entries/`
(record.json + summary.md read in full for each): Masset 2020, Lak 2014, Meyniel & Dehaene
2017, Zajkowski et al. 2017, Fleming et al. 2014, Tervo et al. 2014, Schwartenbeck et al.
2015. Claim family cross-checked: ARC-053, ARC-054, INV-067, INV-068 (`claims.yaml`).
