# Public Explorer ("Lab Window") — maintainer runbook

A static, read-only public view of REE's reviewed claims and evidence, served by
GitHub Pages alongside the existing site. It is **separate from** the internal
`serve.py` cockpit and exposes no operational detail. Full rationale and the
safety boundary: [`docs/public_explorer_policy.md`](../docs/public_explorer_policy.md).

## Pieces

| File | Role |
|------|------|
| `scripts/export_public_explorer.py` | Export pipeline (reads canonical sources → curated JSON). |
| `scripts/public_explorer_config.yaml` | Curation config: scope rules, taxonomy, orientation copy, contribution paths. Edit this to adjust wording or scope. |
| `scripts/test_export_public_explorer.py` | Leak/scope validation suite. |
| `docs/public_explorer/` | Static front-end (`index.html`, `public_explorer.js`, `public_explorer.css`) + generated `data/*.json`. |
| `docs/public_explorer_policy.md` | Public transparency note. |
| `.github/ISSUE_TEMPLATE/*.yml` | Contribution issue forms. |
| `public_explorer_redaction_report.md` | **Local** review artifact (repo root, not published). |

## Regenerate the public export

Run from the `REE_assembly/` repo root. Refresh the evidence index first so the
overlay is current (the exporter degrades gracefully if it is stale/absent):

```bash
bash scripts/governance.sh            # or just: python evidence/experiments/scripts/build_experiment_indexes.py
/opt/local/bin/python3 scripts/export_public_explorer.py --check
```

`--check` builds the export **and** runs the validation suite, exiting non-zero
on any leak or scope violation. Without `--check` it just builds.

Outputs:
- `docs/public_explorer/data/{index,orientation,claims_public,experiments_public,mechanisms_public,help_wanted}.json`
- `public_explorer_redaction_report.md` (repo root — review this; do **not** commit it / it is the human gate)

## Run the tests on their own

```bash
/opt/local/bin/python3 scripts/test_export_public_explorer.py     # standalone
# or:  pytest scripts/test_export_public_explorer.py
```

The suite includes positive controls (known leak strings that the scrub **must**
catch) and negative controls (legitimate science text that must **not** be
over-redacted), plus allowlist/scope/pending-count assertions on the output.

## Preview locally

The front-end is static. Serve the `docs/` tree and open the explorer:

```bash
cd docs && /opt/local/bin/python3 -m http.server 8001
# then open http://localhost:8001/public_explorer/
```

(The relative link to the policy page resolves correctly both locally and under
the `/REE_assembly/` Pages base URL.)

## Manual review BEFORE publishing

1. Open `public_explorer_redaction_report.md`.
2. Read the **"Manual review required"** table — these are allowlisted fields
   (e.g. an experiment summary) that tripped the sensitive-pattern scrub and were
   dropped. Confirm each is a true positive; if a source manifest genuinely
   leaked a hostname/path, consider fixing the source.
3. Sanity-check the "withheld by reason" counts look right (most claims are
   withheld as `status:candidate` and future-stage — that is expected).

## Publish

GitHub Pages serves `/docs` from `master`. Commit the front-end + regenerated
data and push:

```bash
git add docs/public_explorer docs/public_explorer_policy.md \
        scripts/export_public_explorer.py scripts/public_explorer_config.yaml \
        scripts/test_export_public_explorer.py scripts/public_explorer_README.md \
        .github/ISSUE_TEMPLATE docs/_config.yml
git commit -m "public explorer: regenerate export"
git push origin HEAD:master
```

Do **not** commit `public_explorer_redaction_report.md` (it is a local artifact;
it is also git-ignored if you add it to `.gitignore`). Live at:
`https://latent-fields.github.io/REE_assembly/public_explorer/`.

## Notes

- The exporter only **reads** `evidence/` and `docs/claims/` and **writes** to
  `docs/public_explorer/` + repo root — neither write path is covered by the
  runner-heartbeat autostash skip, so no `TASK_CLAIMS` entry is required for the
  writes. Commit promptly all the same.
- It is intentionally **not** wired into `governance.sh`, to keep the
  redaction-report human gate before anything goes public. To change scope,
  edit `public_explorer_config.yaml` (`scope` block) and re-read the policy doc.
