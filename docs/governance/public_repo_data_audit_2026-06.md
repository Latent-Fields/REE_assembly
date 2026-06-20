---
nav_exclude: true
---

# Public-Repository Data Audit -- 2026-06

**Date run:** 2026-06-19T16:14Z
**Auditor session:** `gov-health-1-public-repo-audit-20260619T1604Z`
**Governs:** GOV-HEALTH-1 (clinical-use prohibition / data-protection bright line)
**Source thought (DPIA template):** [`docs/thoughts/2026-06-19_research_health_data_frameworks_for_ree.md`](../thoughts/2026-06-19_research_health_data_frameworks_for_ree.md)
**Plan of record:** [`evidence/planning/ethics_perimeter_plan.md`](../../evidence/planning/ethics_perimeter_plan.md)
**Result:** **CLEAN -- no patient-identifiable or identifiable-human-subject data found in any public-tracked content.**
**Status:** Non-blocking for the V3 green-board. First verification of a previously asserted-but-unverified bright line.

---

## 1. Why this audit exists

GOV-HEALTH-1 asserts a bright line:

> No patient-identifiable data in public repos; no identifiable human data
> without a DPIA-style protocol.

REE is developed by a consultant psychiatrist (HSE Ireland) under the
`github.com/Latent-Fields` org. Until now the bright line was **asserted** in the
claim register and the ethics-perimeter plan, but never **verified** against what
is actually published. This audit closes that gap by inspecting the git-tracked
content of every REE repo and (critically) **verifying each repo's actual GitHub
visibility via the API** rather than assuming it from the namespace.

This is a verification pass. The bright line itself is the policy; this document
is evidence that the policy holds in practice as of the date above.

---

## 2. Scope

**Published surface = git-tracked files in the PUBLIC repos.** The audit respects
`.gitignore` and ignores the untracked working tree (the governance concern is
what is *published*). Visibility was checked via `gh repo view --json visibility`
on 2026-06-19T16:22Z -- **not assumed from the namespace.** Nine repos exist
under the org; **five are public, four are private:**

| Repo | Visibility | Tracked files | In GOV-HEALTH-1 scope |
|------|-----------|---------------|------------------------|
| REE_assembly | **PUBLIC** | 16,520 | yes (primary) |
| ree-v3 | **PUBLIC** | 1,335 | yes |
| ree-v2 | **PUBLIC** | 4,037 | yes |
| ree-v1-minimal | **PUBLIC** | 136 | yes |
| REE_OpenClaw | **PUBLIC** | 83 | yes |
| REE_convergence | private | 274 | scanned (defence-in-depth) |
| ree-experiments-lab (archived) | private | 471 | scanned (defence-in-depth) |
| REE_Working (umbrella) | private | 61 | scanned (defence-in-depth) |
| Strategy | private | 24 | scanned (defence-in-depth) |

The **public surface that GOV-HEALTH-1's "no patient data in public repos" line
actually governs is the five PUBLIC repos** (~22,100 tracked files). The four
private repos were scanned anyway as defence-in-depth (a private repo can be
flipped public, or a member added) -- all clean. Total searched: ~22,940 tracked
files.

> **Correction (2026-06-19T16:22Z).** An earlier draft of this audit asserted
> that all of these repos were public "because they share the `Latent-Fields`
> namespace." That assumption was **wrong** and was replaced with an API
> visibility check -- precisely the unverified-assertion failure mode this audit
> exists to retire. `REE_convergence`, `ree-experiments-lab`, the `REE_Working`
> umbrella, and `Strategy` are **private**. `Strategy` in particular is a
> *separate* private repo (its README states it is "intentionally private");
> it merely appears as an untracked dir (`?? Strategy/`) from the umbrella's
> `git status` because it is a nested independent repo. It holds candid
> strategy / funding / outreach planning material and is correctly private.
>
> **Strategy scan result: CLEAN** -- the only email is a generic organisational
> funding address (`funds@effectivealtruism.com`); the `outreach/` collaborator
> and organisation files are empty templates (`(Names / notes)` placeholders);
> no phones, clinical identifiers, case narratives, or secrets. Because it is
> private, collaborator contact details added there in future are not a
> public-exposure issue -- but keep the repo private and apply GDPR minimisation
> regardless.

**Out of scope (by design):** the project's legitimate synthetic / abstract use
of terms like *harm*, *suffering*, *psychiatric*, *patient*, *care*, *repair* in
architecture and claims prose. REE is an ethics-modelling research substrate;
those words are expected throughout and are not data. The audit targets
**plausible real-data leakage**, not vocabulary.

---

## 3. What was searched

All searches used `git grep` over tracked files in each repo (case-insensitive
where appropriate). Pattern families:

1. **Email addresses** -- `[\w.%+-]+@[\w.-]+\.(com|org|ie|net|edu|gov|io|co|uk)`,
   tallied and individually located.
2. **Phone numbers** -- Irish `+353` / `08x` mobile / `0N NNNNNN` landline, plus
   generic `NNN-NNN-NNNN`, across `*.md *.txt *.json *.yaml *.csv`.
3. **Clinical record identifiers** -- `MRN`, `PPSN`/`PPS number`, `NHS number`,
   `hospital number`, `chart number`/`chart no`, `date of birth`/`DOB:`
   (excluding `mRNA`/`mrn_` code tokens).
4. **Secrets / credentials** -- PEM private-key headers, AWS `AKIA...`, OpenAI
   `sk-...`, GitHub `ghp_...`, Slack `xox...`, and `password=`/`secret=`/`api_key=`
   literal assignments (placeholders/env-var reads filtered out).
5. **Clinical case-narrative free text** -- `N-year-old`, `the patient
   presented/was admitted/reported/denied`, `presented with / to ED / to A&E`,
   `referred by/to Dr...`, `admitted under...`.
6. **Titled person names** -- `Mr|Mrs|Ms|Miss <Surname>` in prose files.
7. **Clinician first-person anecdote markers** -- `a patient of mine`, `one of
   my patients`, `in my clinic`, `patient I saw/treated/assessed`, `referral
   letter`, `session transcript`, `clinic notes`, `case note:`, `presenting
   complaint`.
8. **Irish-specific identifiers** -- Eircode (`A65 F4E2` shape) and PPS-number
   (`7 digits + 1-2 letters`) patterns, with commit-hash/UUID noise filtered.
9. **Real-cohort / service-data markers** -- `dataset of patients`, `cohort of N
   patients`, `n = N patients/service users`, named Irish hospitals / psychiatric
   units, `psychiatric admission/inpatient record/note`.
10. **External-content landing zones** -- enumerated the `imports/` /
    `temp_imports/` directories (REE_assembly) and the `handoff/` / `sources/`
    intake tree (REE_convergence), the highest-risk surface for accidental
    real-data ingress.
11. **Tabular data** -- enumerated all tracked `*.csv` files for person-level
    health-data tables.

---

## 4. What was found

**Nothing patient-identifiable, and nothing requiring remediation.** Every
PII-shaped hit resolved to a legitimate, expected, non-patient category:

| Finding | Where | Adjudication |
|---------|-------|--------------|
| `daniel.delaharpe.golden@gmail.com`, `dgolden@github.com`, `nooarche@users.noreply.github.com` | `contributors/build_contributions.py` (author->name map) and git plumbing | **Author attribution.** The project author's own contact identity, not a data subject. Expected and legitimate. |
| `cowley@cshl.edu`, `mattsmith@cmu.edu` | `imports/temp_imports/nihpp-2023.11.22.568315v1/*` | **Published academic correspondence** from an imported neuroscience preprint (public scholarly metadata). Not patient data. |
| `test@example.com` | test fixture | Reserved RFC-2606 example domain. Not real. |
| "session transcript" (2 hits) | `evidence/planning/goal_pipeline_*_memo*.md`; `WORKSPACE_STATE.md` | Refers to **Claude/agent session transcripts**, not clinical transcripts. False positive. |
| Academic author emails in preprint | as above | Single imported preprint is the only external-content item under `imports/temp_imports/`. |

**Zero hits** for: phone numbers; clinical record identifiers (MRN/PPS/NHS/chart
/DOB); secrets/credentials; clinical case-narrative free text; titled person
names in prose; clinician first-person patient anecdotes; Eircode/PPS patterns;
real-cohort/hospital/service-data markers. **No tracked CSV files exist** in any
repo (no person-level data tables published).

### Conclusion

> As of 2026-06-19, the git-tracked content of all nine REE repositories -- the
> five **public** ones that GOV-HEALTH-1 governs and the four private ones
> scanned as defence-in-depth -- contains **no patient-identifiable data, no real
> clinical notes/transcripts, no real names tied to health context, no referral
> or service data, no identifiable human-subject free text, and no leaked
> secrets.** GOV-HEALTH-1's "no patient data in public repos" bright line is
> **verified to hold** at the current HEAD of every repo.

This is the expected and hoped-for outcome: REE is a synthetic research
substrate, and the published material is theory, code, claims, governance, and
literature synthesis -- not human data.

---

## 5. Notes and limitations

- **Current HEAD only.** This pass inspects the tip of each repo, not full git
  history. The searches above found nothing identifiable to begin with, so there
  is no history-rewrite concern arising from this audit. (Had anything been
  found, the procedure would have been to surface it and stop for instruction
  before any history rewrite -- nothing triggered that path.)
- **Untracked working-tree drafts -- scanned, clean, remain unpublished.** The
  umbrella working tree holds several genuinely untracked, *unpublished* drafts:
  `REE_funding_landscape_and_LTFF_application.md`, the `REE_gamma_*` prompt decks
  (including a psychiatrist-facing one), and `unknown_triage_map_2026-06-02.json`.
  These were scanned with the same email / phone / clinical-narrative patterns as
  a precaution (follow-up 2026-06-19T16:22Z): **zero hits** -- no emails, no
  patient/clinical-record markers, no case narratives. They carry no real
  clinical vignettes. They are not tracked in any repo, so they remain
  unpublished; the same check should be re-confirmed before any future
  `git add`. (Note: `Strategy/` was originally listed here in error -- it is a
  *separate, private repo*, not an unpublished draft; it has been moved into the
  audited-repo table in Section 2 with its own CLEAN result.)
- **Vocabulary is not data.** This audit intentionally does not flag the
  thousands of legitimate uses of clinical/affective vocabulary in REE's
  architecture; doing so would be noise. The signal sought was structured
  identifiers, real contact details, named individuals with health context, and
  free-text records -- none present.

---

## 6. DPIA-style pointer (GOV-HEALTH-1)

GOV-HEALTH-1 and Framework 4 of the source thought require that **if** REE ever
processes personal or health data, a DPIA-style assessment is completed *before*
processing, and that **public repositories must not contain personal, patient,
or service-identifiable data**. The minimum DPIA field template lives in the
source thought
([`docs/thoughts/2026-06-19_research_health_data_frameworks_for_ree.md`](../thoughts/2026-06-19_research_health_data_frameworks_for_ree.md),
Framework 4):

```yaml
processing_purpose:
data_categories:
special_category_data: true/false
lawful_basis:
data_minimisation:
retention_period:
access_controls:
security_controls:
risks_to_data_subjects:
mitigations:
residual_risk:
DPO_or_external_advice_required:
public_repo_exclusion_confirmed:
```

**For this audit, the operative field is the last one:**
`public_repo_exclusion_confirmed: true` -- confirmed by the searches in
Section 3-4. No personal/health data is being processed by REE-v3 (synthetic
substrate work), so no full DPIA is triggered; this audit is the standing
evidence that the public-repo-exclusion sub-clause of GOV-HEALTH-1 is satisfied.

If a future REE workstream ingests any identifiable human data, this audit must
be re-run and a full DPIA completed under
`docs/governance/human_impact_and_research_ethics_register.md` (planned, Phase 3
of the ethics-perimeter plan) before that data goes anywhere near a tracked file.

---

## 7. Re-run recipe

To repeat this verification (recommended at each generation boundary, per
GOV-HEALTH-1 `binds_at_version: v3` "maintained now", and before publishing any
new repo):

1. For each public repo, search tracked files only with `git grep` using the
   pattern families in Section 3 (emails, phones, clinical IDs, secrets,
   case-narrative free text, titled names, clinician anecdotes, Irish IDs,
   cohort/hospital markers, CSV enumeration, external-import landing zones).
2. Adjudicate each hit: author/dev identity and published academic metadata are
   expected; structured clinical identifiers, named individuals + health context,
   and real free-text records are violations.
3. If any violation is found: **do not silently delete.** Record it here, flag it
   to the maintainer, assess git-history exposure, and stop for instruction
   before any history rewrite.
4. Update this file (or a dated successor) with the result.
