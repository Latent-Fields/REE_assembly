# Literature `claim_ids_tested` under-tagging audit

**Date:** 2026-08-09
**Session:** `metaworker-chip-20260809-lit-claim-tag-audit` (chip `chip-20260809-lit-claim-tag-audit`)
**Scope:** `REE_assembly/evidence/literature/*/entries/*/record.json` (2149 records), cross-referenced
against `docs/claims/claims.yaml` (994 claims).

This is an **evidence-tagging** audit, not a governance action. No claim `status` or `confidence`
was edited; those are governance's call. Only `claim_ids_tested` was changed, and the index was
rebuilt so the derived confidences recompute.

---

## Motivating incident

On 2026-08-09 the scheduled `/lit-pull` selected **MECH-143** and **MECH-144** as having zero
literature coverage. They did not. All three of their founding papers were already in the corpus,
sitting under `targeted_review_q_020/entries/` tagged `claim_ids_tested: ["Q-020"]` and never
tagged to the two claims they were cited to establish:

| paper | founds | was tagged |
|---|---|---|
| Duvelle et al. 2019, dorsal CA1 place-cell value-insensitivity | MECH-143 | `["Q-020"]` |
| Jimenez et al. 2018, ventral CA1 anxiety cells | MECH-144 | `["Q-020"]` |
| Knudsen & Wallis 2021, primate abstract value maps | MECH-144 | `["Q-020"]` |

Both claims' `notes` name these papers explicitly, and both carried `evidence: []`.

The selector reads coverage from `claim_ids_tested` — which is correct and deliberate; a
directory-name check was previously measured to false-positive at ~65x. So under-tagging causes two
harms: claims read as zero-coverage and get redundantly re-pulled, and their `literature_confidence`
in `claim_evidence.v1.json` is understated.

**The redundant pull was not hypothetical — it completed.** `REE_assembly 3110162d57`
(*"lit-pull: MECH-143 / MECH-144 hippocampal dorsoventral value coding (6 entries, 5 papers)"*)
landed 6 new entries under `targeted_review_connectome_mech_143/` and
`targeted_review_connectome_mech_144/` before this audit started. So both claims *do* have
literature coverage as of now; what was still missing, and what this audit fixes, is the link to
their own **founding** citations. That link is what makes the provenance in each claim's `notes`
resolvable, and what stops the same re-pull recurring.

---

## Method: three detection signals, only one of which works

I ran three corpus-wide scans. Recording all three, including the two that failed, because the
failures are the substantive methodological result — **the two obvious heuristics cannot detect the
incident class at all.**

### Signal 1 — record sits in a `targeted_review_<claim>` directory that omits that claim (FAILED)

**70 findings across 21 directories.** Almost entirely false positives. A review directory is a
**campaign folder**, not a claim assertion: a pull opened for one claim routinely files papers that
bear on neighbouring claims. Classified:

- 23 are **parent/sub-claim** pairs — `targeted_review_connectome_mech_074` holding records tagged
  `MECH-074a`/`074c`/`074d`. The specific sub-claim tag is *more* correct, not less.
- 47 are **a different claim entirely**, and in nearly all of them the entry filename itself names
  the claim it is tagged to — `targeted_review_mech_457_consolidation/2026-07-29_mech_476_...`
  tagged `["MECH-476"]`. Correctly tagged; the folder is just where the campaign put it.

**Does not catch the incident:** the Q-020 records sit in `targeted_review_q_020` and *are* tagged
`Q-020`. Zero flags.

### Signal 2 — entry filename names a claim absent from `claim_ids_tested` (FAILED)

**17 mismatches** out of 1861 records whose filename parses to a claim id (of 2149 total). Sharper
than signal 1, and a genuinely useful hygiene check, but most are again the legitimate sub-claim
case (`mech_057` → `MECH-057a`, `sd_003` → `SD-003-prereq`, `mech_025` → `MECH-025b`).

**Does not catch the incident:** entry `2026-03-29_q020_value_free_map_duvelle2019` names `q020` and
is tagged `Q-020`. Consistent. Zero flags.

### Signal 3 — claim's own `notes` cite a paper that is in the corpus but not tagged to it (WORKS)

Extract author-year citations from each claim's `notes` / `resolution_note` /
`evidence_quality_note` / `conflict_note`; index the corpus by (first-author surname, year); flag
where the paper exists but the citing claim is absent from its `claim_ids_tested`.

**187 findings across 132 claims.** Of those, **48 findings across 36 claims are on claims that have
zero literature records today** — i.e. exactly the MECH-143/144 shape, claims that will be selected
for a redundant `/lit-pull` while their founding citations already sit in the corpus.

This is the only signal that reconstructs the provenance link, because the link lives in the
*claim's* prose, not in any file path.

---

## What was changed

Three records, verified individually by reading each `summary.md` and confirming the paper bears on
the claim. No bulk retag was applied.

**1. Duvelle 2019 → `MECH-143` added in place.**
`targeted_review_q_020/entries/2026-03-29_q020_value_free_map_duvelle2019/record.json`,
`claim_ids_tested: ["Q-020"] → ["Q-020", "MECH-143"]`. The record's `evidence_direction` is
`supports`, which is correct for both claims, so no split was needed. The summary already states the
conclusion verbatim: *"dorsal CA1 is value-free (supporting ARC-007), ventral CA1 and primate
hippocampus show value-geometric coding (supporting MECH-073)."*

**2 & 3. Jimenez 2018 and Knudsen & Wallis 2021 → new `MECH-144` records**, not an in-place tag:

- `targeted_review_mech_144/entries/2026-08-09_mech_144_valence_geography_jimenez2018/`
- `targeted_review_mech_144/entries/2026-08-09_mech_144_abstract_value_map_knudsen2021/`

### Why those two needed a split — the direction-sign trap

Both Q-020 records carry `evidence_direction: "weakens"`. That is correct **for Q-020**: the papers
weaken Q-020's ARC-007 "hippocampus is value-free" framing. But they weaken it *precisely by
supporting MECH-144*, the claim they found. One finding, opposite signs against two propositions.

`evidence_direction` is a **single per-record field** that the indexer applies uniformly to every id
in `claim_ids_tested`. `evidence_direction_per_claim` exists in `build_experiment_indexes.py` but is
read only on the **experiment-manifest** path (line ~1390); `LiteratureRecord` (line ~681) has no
such field, and literature direction is aggregated per claim at lines ~2549-2552.

So adding `MECH-144` to the existing `weakens` records would have registered its two founding
papers as **contradicting** it — with `consistency = |0-2|/2 = 1.0`, i.e. *high-confidence*
literature against the claim. That is strictly worse than the zero-coverage state it was meant to
fix: it would have produced a false `lit_non_support` signal on a live claim.

Splitting the record is the corpus's own established convention for this, not an invention here.
Measured: **269 papers appear in more than one record, 93 of them with differing
`evidence_direction` across records.** Precedents include Camille 2004 (`supports` ARC-029 /
`weakens` Q-090) and Mattar & Daw 2018 (`supports` in twelve records, `weakens` in the Q-011 one).

Confidences on the new records were set deliberately rather than copied:

- Jimenez → MECH-144: **0.72**, unchanged from the Q-020 sibling. Mapping fidelity rises
  (0.62 → 0.68 — MECH-144 is stated at the ventral-compartment level the paper measures, so the
  dorsal/ventral abstraction gap that penalised the Q-020 mapping does not apply), but transfer risk
  is identical, which holds the total.
- Knudsen → MECH-144: **0.70**, *lowered* from the sibling's 0.78. MECH-144 is specifically a
  ventral-compartment claim and this is primate hippocampus with no dorsoventral localisation — the
  compartment specificity that makes it fit MECH-144 is exactly what the paper does not establish.
  Mapping fidelity 0.68 → 0.60, transfer risk 0.38 → 0.42.

---

## Index rebuild, and a metric trap worth knowing

`build_experiment_indexes.py` rerun: literature entries **2149 → 2151**, 12 derived files changed
(within the ~13 expected; 11 further files were already dirty from another session and were left
untouched). Resulting movements:

| claim | `literature_confidence` | `lit_posterior.mean` | overall |
|---|---|---|---|
| MECH-143 | 0.79 → **0.664** | 0.363 → **0.419** | 0.663 → 0.568 |
| MECH-144 | 0.667 → **0.811** | 0.573 → **0.708** | 0.538 → 0.678 |
| Q-020 | unchanged | unchanged | unchanged |

Q-020 is unchanged, which is the check that the split-record approach worked: its two `weakens`
records were left exactly as they were.

One large-looking-but-benign diff to expect in `architecture_gap_register.v1.json`: **MECH-144
drops off the register entirely** (92 → 91 items) now that it has evidence, and 52 downstream
`gap_id`s shift by one as a result. `AGR-####` is a rank position, not a stable identifier — the
only reference to one outside the register already treats it that way
(`recovered_stranded_manifests/README.md:135`, *"slides it from `AGR-0001` to `AGR-0011`"*), so
nothing breaks. `evidence_backlog.v1.json` gains MECH-143 under `dormant_high_conflict`, which is
the contested state described below.

**MECH-143's `literature_confidence` went DOWN after adding a supporting paper.** That is correct
behaviour, and the reason is a genuine trap for anyone reading these numbers:
**`literature_confidence` measures consistency × quality, not favourability.** The legacy formula
(`build_experiment_indexes.py` ~2549-2558) is
`consistency = |supports - weakens| / (supports + weakens)`, so *unanimity* scores high **regardless
of which way the literature points**. Before this change MECH-143's literature was 0 supports /
2 weakens / 2 mixed — unanimous among directional entries, consistency 1.0, hence 0.79. Adding
Duvelle makes it 1/2/2, consistency 0.33, hence 0.664.

So the drop records that MECH-143's literature is now *split* rather than uniformly against it,
which is a more accurate description than the 0.79 was. The quantity that actually tracks
favourability is `lit_posterior.mean`, and it moved the right way (0.363 → 0.419). Do not read a
falling `literature_confidence` as evidence weakening.

**MECH-143 is now genuinely contested and that is governance's call, not this audit's.** Its five
literature entries stand at 1 supports (Duvelle 2019, its founding citation) / 2 weakens (Silva
2026, Mamad 2017) / 2 mixed (Masala 2026, Bhattarai 2019) — the morning pull's papers point against
the claim its founding paper established. No `status` or `confidence` field in `claims.yaml` was
touched here.

---

## What was deliberately left alone

**The other 184 provenance findings (129 claims), including the 36 zero-coverage claims listed
below.** A claim citing a paper is not proof the paper *evidences* it — papers get cited as
background, as contrast, or for a mechanism aside. Each case needs its `summary.md` read and, as
MECH-144 demonstrates, a per-case direction-sign judgment that can invert the result. Bulk-applying
this scan would inject exactly the false-`weakens` corruption described above at scale. Left as a
reviewed queue, not an automated fix.

The 36 zero-coverage claims whose own notes cite a corpus paper (highest-value subset — these are
the ones that will trigger redundant `/lit-pull` selections):

`ARC-031` `ARC-037` `ARC-052` `ARC-073` `ARC-075` `ARC-105` `INV-039` `MECH-125` `MECH-136`
`MECH-145` `MECH-146` `MECH-233` `MECH-248` `MECH-249` `MECH-289` `MECH-298` `MECH-299` `MECH-300`
`MECH-301` `MECH-312b` `MECH-312c` `MECH-312d` `MECH-345` `MECH-351` `MECH-403` `MECH-432`
`MECH-461` `SD-019a` `SD-032` `SD-033` `SD-038` `SD-041` `SD-043` `SD-051` `SD-052` `SD-081`

(Note `MECH-233` also cites Jimenez 2018 — the same paper handled here, a second instance of the
identical pattern.)

**The signal-1 and signal-2 findings.** Assessed above as dominated by legitimate sub-claim tagging
and campaign-folder filing. No action.

**Claim `status` / `confidence` / `evidence:` arrays in `claims.yaml`.** Governance's call. This
audit changed evidence tagging only and let the indexer recompute.

**A pre-existing schema divergence, noted not fixed.** `evidence/literature/schemas/v1/literature_evidence.schema.json`
declares `source.additionalProperties: false` with no `pmid`/`pmcid` in its allowed set, yet **484
records carry `pmid`**. The schema is not enforced by any validator in the repo (only
`evidence/planning/scripts/build_connectome_literature_pull.py` references it). The new records
mirror their siblings and include `pmid`. Widening the schema is out of scope here but is a real
loose end.

---

## Recommended follow-on

1. **Work the 36-claim zero-coverage list** above, case by case, same method as the three fixed
   here: read the `summary.md`, confirm the paper bears on the claim, and check the direction sign
   before choosing in-place tag vs. split record. This is `/lit-pull`-adjacent work with no
   re-deriver, so it needs a chip.
2. **Consider a pre-pull check in `/lit-pull`**: before selecting a claim as zero-coverage, run
   signal 3 against it and surface any already-corpus papers its notes cite. That converts this
   audit from a one-off into a standing guard, and would have prevented the 2026-08-09 selection.
3. **`evidence_direction_per_claim` on the literature path** would remove the need to split records
   at all. It is a real substrate change to `build_experiment_indexes.py` needing contract tests,
   and the split-record convention works today — worth doing only if the split-record count grows.
