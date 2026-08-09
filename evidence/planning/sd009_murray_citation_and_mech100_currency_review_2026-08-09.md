# SD-009 / MECH-100: Murray citation integrity + MECH-100 evidence-currency review

**Status: REVIEW COMPLETE. Bibliographic corrections and a `needs_review` flag HAVE been applied; NO claim status was changed and NO evidence confidence was re-scored. The two open questions at the end are for `/governance`.**

| | |
|---|---|
| Date | 2026-08-09 |
| Session | `metaworker-chip-20260809-sd009-897-followon` (headless, metaworker-dispatch) |
| Chip | `chip-20260809-sd009-897-followon` |
| Commissioned by | `evidence/planning/failure_autopsy_V3-EXQ-897_2026-08-08.{md,json}`, `adjacent_recommendations` items 1 and 2, both `user_confirmed: true` |
| Claims touched | SD-009 (candidate), MECH-100 (stable — **unchanged**) |

---

## Item 1 — the "lit-pull bookkeeping gap" is a citation-integrity defect

The autopsy recorded this as bookkeeping: a Murray citation doing rhetorical work in prose that "was never entered into `claim_evidence.v1.json` as a tracked `targeted_review_sd_009` entry". Its recommendation was to "register directly (citation already identified) rather than commissioning a full `/lit-pull`". The chip that carried it forward added the right instruction — *verify the exact citation from SD-009's own text/notes before searching, do not guess a paper* — and verification is what changed the finding.

### 1a. The cited article does not exist

`claims.yaml` MECH-100 `notes` carried:

> Predictive coding alone does not produce object-discriminative ventral stream representations without categorical top-down signals (Murray et al. 2004, TICS 8:56–61).

*Trends in Cognitive Sciences* volume 8, issue 2 (February 2004) contains no paper by any Murray, and pages 56–61 do not delimit a single article in it. Complete PubMed listing of the issue:

| pages | article |
|---|---|
| 47–49 | Kourtzi, *"But still, it moves"* |
| 49–51 | Scholl, *Can infants' object concepts be trained?* |
| 51–53 | Munhall & Buchan, *Something in the way she moves* |
| 57 | Toates, *"In two minds"* (letter) |
| 58–59 | Grainger & Whitney, *Does the huamn mnid raed wrods as a wlohe?* |
| 60–65 | Stevens & Hauser, *Why be nice? Psychological constraints on the evolution of cooperation* |
| 66–70 | DeLoache, *Becoming symbol-minded* |
| 71–78 | Johnson-Frey, *The neural bases of complex tool use in humans* |
| 79–86 | Maravita & Iriki, *Tools for the body (schema)* |
| 87–93 | French & Jacquet, *Understanding bilingual memory* |

Issue 3 (March 2004) begins at page 95. So the range 56–61 straddles a letter and an unrelated review, and there is no Murray article anywhere in the volume. PubMed's citation matcher returns `NOT_FOUND` for `{Trends Cogn Sci, 2004, vol 8, p.56}` under both journal spellings, with and without the author.

### 1b. The tracked entry that did exist had three wrong bibliographic fields

`evidence/literature/targeted_review_connectome_mech_100/entries/2026-03-29_mech_100_ventral_stream_categorical_murray2004/record.json` was filed against **MECH-100** (not SD-009 — the autopsy was right about that part). Its `source` block named the right authors, year and venue, but:

| field | was | is |
|---|---|---|
| `source.title` | "What we know and do not know about the functions of the perirhinal cortex" | "Visual perception and memory: a new view of medial temporal lobe function in primates and rodents" |
| `source.venue` | Annual Review of Neuroscience | Annual Review of Neuroscience 30:99-122 |
| `source.doi` | `10.1146/annurev.neuro.29.051605.112951` | `10.1146/annurev.neuro.29.051605.113046` |
| `source.url` | PMID 17645520 | PMID 17417938 |

PMID 17645520 is *"Hepatic venous outflow reconstruction in right lobe graft without middle hepatic vein"*, Hepatology Research 37(12):1044-51 — an unrelated liver-transplantation paper. The old DOI differs from the real one only in its final digits and does not resolve to this article.

The paper the record was reaching for is unambiguous from its authors, year, venue and — decisively — from its own `summary.md`, whose body describes the perirhinal feature-ambiguity argument of the 2007 Annual Review in detail. **Murray EA, Bussey TJ, Saksida LM (2007), *Visual perception and memory: a new view of medial temporal lobe function in primates and rodents*, Annual Review of Neuroscience 30:99–122, PMID [17417938](https://pubmed.ncbi.nlm.nih.gov/17417938/), DOI [10.1146/annurev.neuro.29.051605.113046](https://doi.org/10.1146/annurev.neuro.29.051605.113046).** Verified against PubMed 2026-08-09.

### 1c. The consequence that is not merely bibliographic

That entry's own `summary.md` recorded, as its third limitation, that the TICS 2004 paper "is a different paper from this Annual Review — the 2004 TICS paper more directly addresses the predictive coding vs. categorical supervision question, but it was not available in the search results." That assumption is now falsified. The 2007 review is not a stand-in for a stronger uncited source; **it is the only source MECH-100's biological grounding has ever had.**

And the two propositions are not the same. The review shows that perirhinal conjunctive representations are shaped by *discrimination demands* rather than by passive exposure — lesions impair feature-ambiguous discriminations and spare feature-distinct ones, hippocampal lesions impair neither. The prose sentence asserts something narrower and stronger: that *predictive coding specifically* fails to produce object-discriminative representations absent categorical top-down signals. No registered entry evidences that. The entry's confidence of 0.62 was assigned on the assumption that a stronger source sat behind it.

### 1d. What was applied

- **New SD-009 entry** — `evidence/literature/targeted_review_sd_009/entries/2026-08-09_sd_009_perirhinal_categorical_object_representation_murray2007/{record.json,summary.md}`, correctly attributed, `evidence_class: connectome_mechanistic_review`, `evidence_direction: supports`, **confidence 0.50**, `mapping_fidelity 0.45`.

  Deliberately below the 0.62 the same paper carries against MECH-100, and the reason is specific to SD-009 rather than to the source. SD-009 is a *design decision* naming one particular auxiliary head. The review supports the necessity of *some* discriminative pressure — which since 2026-07-18 SD-070's own grounding heads (class-balanced CE over hazard/resource presence and bucketed Chebyshev distance, plus a VICReg penalty) already supply by another route. V3-EXQ-897 tested exactly the residual: whether a dedicated event-CE head adds anything on top. It found held-out frozen-probe decodability above floor in both arms with OFF ≥ ON on 3/3 seeds. Literature and experiment now bear on different granularities of the same claim, and the literature must not be read as covering the gap.

  Before this entry SD-009 had **no** biological or neuroscientific literature at all — `literature_confidence` 0.724 from two `lit:computational_model` entries (ADAT/Kim 2022, CURL/Laskin 2020).

  **A caution about the resulting number, because it moves the wrong way.** After the `--index-only` rebuild SD-009 reads `literature_confidence` **0.773** (up from 0.724) and `overall_confidence` **0.66** (up from 0.59). That rise is an artefact of the aggregation, not a strengthening: the Beta posterior counts a third `supports` entry and is insensitive to the fact that this one is deliberately the weakest of the three, scored low *because* it does not reach SD-009's specific commitment. The qualitative finding runs opposite to the metric — the single biological citation this claim family leaned on for four months was unverifiable, and the real source supports only the general antecedent that SD-070 already satisfies by another route. Anyone reading SD-009's confidence trend should read this entry's `mapping_caveat` alongside it.

- **MECH-100 record corrected in place** — four bibliographic fields, with the previous values preserved verbatim under a new `metadata_correction` key. `evidence_direction`, `confidence`, `mapping` and `failure_signatures` are **untouched**. `entry_id` keeps its `_murray2004` suffix because other artefacts key on it as an identifier, not as a citation.
- **`summary.md` heading and third limitation corrected**, with a dated correction banner.
- **`claims.yaml` prose citation corrected** in MECH-100 `notes`, inline-flagged that the 2007 review supports the weaker proposition.

---

## Item 2 — MECH-100 evidence currency (review only, no status change)

MECH-100 is `status: stable`, promoted provisional → stable on 2026-04-03 on `conf=0.817, conflict_ratio=0, 4 exp all supports, 3 lit entries`.

All four experimental entries are from **2026-03-18 and 2026-03-20**:

| run_id | timestamp | direction |
|---|---|---|
| `20260318T083631Z_v3_exq_020_event_contrastive_v3` | 2026-03-18T08:36:31Z | supports |
| `20260318T180301Z_v3_exq_022_combined_contrastive_lstsq_v3` | 2026-03-18T18:03:01Z | supports |
| `20260320T165149Z_v3_exq_020_event_contrastive_v3` | 2026-03-20T16:51:49Z | supports |
| `20260320T171130Z_v3_exq_022_combined_contrastive_lstsq_v3` | 2026-03-20T17:11:30Z | supports |

**SD-070 landed 2026-07-18** — roughly four months later. Its `functional_restatement` documents the P0 those runs were gathered under as collapsing z_world to `participation_ratio ~1.06` at `world_dim=128` (untrained: 9.21; contrast_ratio 0.1222 → 0.0726), and names the SD-009 event-contrastive target itself as the *first* of the three faults driving it: `transition_type` is a property of the transition (t−1 → t) while z_world is a static single-frame encoding, and an MLP-128 probe on raw `world_obs` with no encoder in the path scores at or below chance for that label (lift −0.014 three-class, −0.060 on a repaired six-class map), while the same labels probe at +0.240 / +0.427 from the BODY delta that SD-005 routes to z_self.

So MECH-100's stable status rests entirely on evidence measured under a training recipe the substrate has since replaced *for cause*, where the cause names this claim's own mechanism. **V3-EXQ-897 is the first re-measurement under the fixed substrate**, and it reads the other way: decodability above floor in both arms, OFF ≥ ON on 3/3 seeds (deltas −0.025 / −0.010 / −0.005) — sign-consistent but statistically imprecise, hence `direction=unknown` rather than `weakens`, and MECH-100 was not tagged by that run.

Two further details worth a governance reader's eye. SD-009 — the same underlying claim in the design register, sharing two of these four runs — was already demoted provisional → candidate on 2026-08-08. And in `claim_evidence.v1.json` all four MECH-100 runs carry `outcome=FAIL` with `direction=supports` (`pass_runs: 0`, `fail_runs: 4`), one annotated `"direction/status mismatch"`, so the aggregate is worth going behind.

**Applied:** `live_status.needs_review: true` with a `needs_review_reason`, plus a full `evidence_quality_note`. **Not applied:** any status change. Per the chip's own instruction and CLAUDE.md, a stable claim is not demoted outside a governance cycle.

---

## Open for `/governance`

1. **Does MECH-100's `stable` still hold?** Options, in the order the 2026-07-18 channel-mismatch doc framed them: leave stable with the caveat recorded; apply a candidate-stale flag per that doc's option (B); or queue a re-verification run of the EXQ-020/022 design under the SD-070 recipe as the discriminator. This chip takes no position beyond noting that the evidence base is uniformly pre-fix and the one post-fix measurement points the other way.
2. **Should the MECH-100 literature entry be re-scored?** Its 0.62 was set assuming a stronger uncited source existed. It does not. Re-scoring a stable claim's literature confidence is a disposition, not a bibliographic fix, so it is left open.

## Out of scope, flagged not fixed

`claims.yaml` **MECH-103** (line ~11863) cites "cross-modal ventral stream binding (Murray et al. 2004)" — a different topic (multisensory convergence, plausibly Micah M. Murray rather than Elisabeth A. Murray) on a different claim, with no tracked literature entry found. Not investigated: outside this chip's scope. Given that the one Murray 2004 citation that *was* checked proved non-existent, this one is worth verifying before it is relied on.

## Verification trail

Every bibliographic assertion above was checked against PubMed on 2026-08-09 via the PubMed MCP tools (`search_articles`, `get_article_metadata`, `lookup_article_by_citation`), not from memory. PMIDs cited: 17417938 (the real source), 17645520 (the wrong URL's target), and the ten-article listing of TICS 8(2) at 15588804–15588813.
