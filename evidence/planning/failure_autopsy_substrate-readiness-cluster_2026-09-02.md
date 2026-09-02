# Failure autopsy -- substrate-readiness diagnostic cluster (14 runs, 2026-04-21 to 2026-06-04)

Generated 2026-09-02T05:04:59Z. Status: **confirmed** (interactive gate, 2026-09-02).
Red-team pass: Fable, verdict **CONTESTED** -- accepted, and the headline finding is withdrawn.

Scope note: `retrospective_diagnostic_selfroute_audit_2026-06-06.md` had already classed this
family "low priority" and recommended sampling rather than per-run autopsies. This is therefore
**one cluster target, not 14**. Dry-run gate: none is a smoke (`dry_run` absent throughout, a
May-2026 vintage artefact; no `_dry_` file exists for any family).

## What is true

**PASS is a plumbing verdict in 12 of 14, by construction.** Criteria are `is not None`, shape
equality, `isfinite`, exact arithmetic identity against a hand-written table (`abs(actual-expected)
< 1e-9`), counter increments, and truth tables. Thirteen of the fourteen complete in
**0.684-2.539s** with no episodic loop -- they are in-process API exercises. Two genuine exceptions
on the science: 613 UC3/UC4 (held-out accuracy 0.891 against a random baseline, gate 0.50) and,
weakly, 542/542a UC4.

**Every driver hardcodes `evidence_direction = "supports" if all_pass else "weakens"`** on its
tagged claims, so a wiring check emits a claim-bearing direction.

**The duplicates are re-emissions, not replicates.** The 545 pair differ on 0 of 37 metric leaves,
the 546 pair on 0 of 82; the 542a triple is one bit-identical pair plus a sibling differing at the
7th-8th significant figure. No seed varies anywhere.

## What is NOT true -- the alarm this autopsy first raised, and withdrew

The first draft asserted that these plumbing passes inflate the headline `direction_counts` a
reader sees, with MECH-313 as the sharpest case ("5 supports against `genuine_exp_count` 0").
**That is wrong, and the containment is complete rather than partial.** `direction_counts` and
`source_counts` are built from entries with `scoring_excluded` **already filtered**. MECH-313's
5 supports are its five **literature** entries (eysenbach2018, haarnoja2018, parkerholder2020,
tervo2014, astonjones2005); its `source_counts` read `{experimental: 0, literature: 6}` and
`entries_total: 6`; both the 544 and 544a rows carry `scoring_excluded=diagnostic_probe`.
**Nothing from this family weights any claim.**

Governance had also already applied the remedy: 545x2, 546x2 and 547 were reclassified
`non_contributory` in the 2026-05-11 walk (`d72741c9e0`), 542a x3 were authored that way, and
613/617/639 carry no `claim_ids`. The claim-bearing `supports` residue is exactly **three
manifests -- 542, 544, 544a** -- i.e. hygiene, not a class-level defect.

A related correction: the pre-routing check C1 reported that `v3_exq_544a` had never scored, and
the first draft repeated it. **544a did run**, on 2026-05-29
(`v3_exq_544a_..._v3_20260529T154903Z.json`, PASS, present in the index).

## What survives -- the durable finding

**All 14 fail the Experimental Recording Standard always-core.** `substrate_hash`,
`substrate_commit` and `config` are absent from every one; `seeds` from 13 of 14. The mechanism is
a shared authoring template: each driver calls
`write_flat_manifest(..., config=manifest.get("config"), seeds=None)` where no `"config"` key was
ever set, so both provenance kwargs are `None` **by construction**. None of the 14 carries
`interpretation` / `preconditions[]` / `criteria_non_degenerate`, so the indexer's adjudication
flag could never fire on the class.

## Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | intact (untested) -- and in practice none reaches a scored count |
| Biological reference | present (C3 check corrected an earlier `absent`) |
| Implementation | complete -- the APIs exist and respond |
| Environment | n/a -- no episodic loop |
| Measurement | misleading -- plumbing verdicts in 12/14 |
| Integration | isolated |
| Scale | n/a |

**Failure-location (GOV-FAILLOC-1): MEASURES.** Not chargeable to REE.

## Routing (confirmed at gate)

`implement-substrate`, **priority 3, severity cosmetic**. Create
`readiness_driver_manifest_provenance_template`: fix the shared template so readiness runs stamp
always-core provenance via `experiments/_lib/manifest_core.stamp_recording_core(...)`. Severity is
deliberately `cosmetic` and not `corrupting`: no evidence is weighted by these runs, so the defect
costs reproducibility and auditability, not evidence quality, and it must **not** gate unrelated
experiments. Secondary hygiene (a readiness gate should emit `non_contributory` rather than a
claim-bearing direction) is noted in the entry, explicitly flagged as hygiene given the withdrawal.
