# Divergent manifest adjudication -- ree-cloud-2, 2026-09-09

**Triaged:** 2026-09-09T08:44Z -- 09:10Z, session `xenodochial-austin-8c5984`
(chip `chip-20260909-cloud2-divergent-manifests`)
**Source:** `ree-cloud-2` (hcloud `ree-worker-2`, 116.203.216.181),
`~/REE_Working/REE_assembly`.
**Probe:** `REE_assembly/scripts/runner_git_health.py`, run as part of the
2026-09-09 morning digest's fleet git-health sweep.

Third instance on this worker of the same class. Direct sibling of
[`README_ree-cloud-2_2026-08-09.md`](README_ree-cloud-2_2026-08-09.md) Section 2
(the `v3_exq_850_..._20260801T005937Z_v3` adjudication), and the same underlying
`git pull` retry-without-restore defect as
[`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md).

**Verdict up front: BOTH divergences are BENIGN. Origin is a strict superset in
both cases, and NEITHER divergence changed a recorded PASS/FAIL outcome.** No
`governance_flag` is implied. Nothing was deleted; nothing was landed.

---

## 0. Method (why this is a diff, not an eyeball)

The probe is explicit that a run_id's origin candidates are **not
interchangeable**, so each local copy was diffed against **all four**:

| candidate | on origin? |
|---|---|
| `evidence/experiments/<run_id>.json` (flat, top-level) | yes |
| `evidence/experiments/<dir>/runs/<run_id>/manifest.json` (pack) | yes |
| `evidence/experiments/<dir>/runs/<run_id>/metrics.json` (pack sibling) | yes |
| `evidence/experiments/<dir>/runs/<run_id>/summary.md` (pack sibling) | yes |
| `evidence/experiments/<dir>/<run_id>.json` (**the local path**) | **no -- never tracked** |

The local copy sits at a **fifth, untracked path shape** -- inside the experiment
directory but *not* under `runs/`. That path has never existed on origin for
either run, which is why the probe grades it as untracked-with-a-known-run_id
rather than as a modification.

Both local files were **copied off the box before anything else was touched**, and
verified byte-identical (`shasum -a 256` locally vs `sha256sum` on the worker):

```
16aa4b947ae0c264998d981e55de08c3423f8a445273a2e5c8780fe9bdeb464d  603v
286bafd0f18df5d0588a70b101d77314a7146b1fca08dd986cd6f7a140e9bbf3  862b
```

Comparison was a **deep structural diff** of the parsed JSON (full recursive
value equality on every shared key), not a textual diff -- the two sides are
serialized with different indentation, so a textual diff is uninformative
(603v's local copy is 156,962 B against origin's 108,309 B while carrying
*fewer* keys).

Origin blobs were read from `origin/master` directly (`git show
origin/master:<path>`), not from the Mac working tree; the Mac's working-tree
copies were separately confirmed equal to the origin blobs, so no HEAD/worktree
skew is in play.

---

## 1. `v3_exq_603v_mech357_eligibility_trace_repair_validation_20260827T184708Z_v3` [PASS] -- BENIGN

**Result of the structural diff against origin's flat manifest:**

```
local keys: 50    origin keys: 51
only in LOCAL : []                          <-- local carries NOTHING origin lacks
only in ORIGIN: ['evidence_direction_note']
shared keys with differing values: ['evidence_direction']
```

| field | cloud-2 (local) | origin (flat + pack) |
|---|---|---|
| `outcome` | `PASS` | `PASS` (pack: `status: PASS`) |
| `evidence_direction` | `supports` | `non_contributory` |
| `evidence_direction_note` | *absent* | present (governance disposition) |
| everything else (50 keys incl. `interpretation`, `arm_results`, `per_seed`, `config`, `trace_window_stats`, `acceptance`, `z_goal_stream`) | identical | identical |

**The outcome is `PASS` on BOTH sides.** The divergence did not touch the
recorded verdict, so this is not the governance-relevant case.

**Origin's value is the ratified one.** Origin's `evidence_direction_note` reads:
2026-08-28 governance cycle `governance-cycle-20260828` adjudicated
`evidence_direction` to `non_contributory` per CONFIRMED
`failure_autopsy_V3-EXQ-603v_2026-08-28.json` (`dry_run_checked: true`), ratified
at that cycle's Step 2b walk -- the manifest's own `supports` is adjudicated
**down**, because V3-EXQ-603v is an INSTRUMENT repair (an eligibility-trace fix
validated against its own pre-registered `failure_record` target), not claim
evidence for MECH-357. That autopsy exists on origin with `status: "confirmed"`.

So cloud-2's `supports` is simply the **pre-governance** runner self-declaration:
the file predates the 2026-08-28 adjudication and was never updated because it
lives at a path nothing writes to.

**Verdict: origin authoritative, local copy is residue. Nothing landed, nothing
deleted.**

---

## 2. `v3_exq_862b_q040c_dacc_pe_weight_delta_correlation_20260828T223750Z_v3` [FAIL] -- BENIGN

Identical shape.

```
local keys: 22    origin keys: 23
only in LOCAL : []
only in ORIGIN: ['evidence_direction_note']
shared keys with differing values: ['evidence_direction']
```

| field | cloud-2 (local) | origin (flat + pack) |
|---|---|---|
| `outcome` | `FAIL` | `FAIL` (pack: `status: FAIL`) |
| `evidence_direction` | `weakens` | `non_contributory` |
| `evidence_direction_note` | *absent* | present |
| everything else (22 keys incl. `per_run`, `acceptance`, `substrate_identity`, `supersedes`) | identical | identical |

**The outcome is `FAIL` on BOTH sides.** Again, no verdict changed.

Origin's note: VOIDED by confirmed autopsy `failure_autopsy_V3-EXQ-862b_2026-08-29`
(landed `REE_assembly f3a2aa2aa6`), ratified at the `/governance` walk
2026-08-29T15:46Z -- **the driver's pre-registered `weakens` is explicitly
overridden** to `non_contributory`. Fourth instrumentation failure of the Q-040.c
lineage: the manipulation engaged but the DV is structurally insensitive
(pe's maximum attainable variance share of `||dACC bias||` is <= 1e-6). Q-040 stays
open; `epistemic_category` set to `answer_state`. That autopsy is on origin with
`status: "confirmed"`.

Cloud-2's `weakens` is therefore **exactly the pre-override value** -- the file is
a snapshot from before the governance walk that overrode it.

**Verdict: origin authoritative, local copy is residue. Nothing landed, nothing
deleted.**

---

## 3. Why nothing was landed (and why that is not the same as the 899 case)

The 2026-08-09 sibling exercise LANDED `v3_exq_899_...` because that run had
**zero** counterpart on origin at any path -- a genuinely stranded 5.2h run.

These two are the opposite: every one of the four origin candidates exists, the
packs are present (so the run is **not** inert to the indexer -- cf. [memory]
`reference-indexer-reads-runs-pack-not-flat`), and `only_local == []` proves the
local copies contain no unique content. There is nothing to recover.

The phantom-completion hypothesis the probe raises ([memory]
`reference-phantom-completion-crash-before-manifest`) is **excluded** for both:
neither local file is a partial write. Both parse, both carry their full payload
(603v: complete `interpretation` block with 6 preconditions carrying
`measured`/`threshold`/`met`, plus `arm_results`/`per_seed`; 862b: complete
`per_run` and `acceptance`), and both agree with origin on every key except the
one governance field.

**Both untracked copies were deliberately LEFT IN PLACE, not deleted** --
CLAUDE.md remedy (a), "never drop on a judgement call". They are non-evidence
residue, not a loss risk, so there is no urgency to clear them.

## 4. Suppression, so the probe stops re-escalating

Two records added to
[`../git_health_adjudicated_divergences.json`](../git_health_adjudicated_divergences.json),
keyed on host/repo/run_id/**content_sha256** (all four). If either untracked file
is ever *edited*, its hash changes and the finding re-escalates -- which is the
intended behaviour, not a gap.

## Related

- [`README_ree-cloud-2_2026-08-09.md`](README_ree-cloud-2_2026-08-09.md) -- Section 2 is the direct precedent for this verdict; Section 1 is the contrasting stranded-run case
- [`README_ree-cloud-2_2026-07-30.md`](README_ree-cloud-2_2026-07-30.md) -- same worker, same underlying defect
- `REE_assembly/scripts/runner_git_health.py` -- the probe; `load_adjudicated_divergences()` reads the suppression registry
