# ree-v3 orphaned `autostash` stash triage

**Triaged:** 2026-07-28T05:21Z (session `dazzling-solomon-8a0090`)
**Repo:** `/Users/dgolden/REE_Working/ree-v3`
**Trunk at triage time:** `origin/main` = `04435e0` (`docs: nightly /update-docs 2026-07-28`)
**Entries triaged:** 5 (all labelled `autostash`)

---

## The defect being triaged

A concurrent `git pull --rebase --autostash` (the experiment runner's sync path,
`ree-v3/experiment_runner.py:971/1017/1037`) stashes a session's uncommitted work. When the
pop fails, the content stays in the stash list and **no error reaches the session that owned
it** -- `git status` simply shows the files unmodified, so the work reads as silently
vanished.

Confirmed live 2026-07-27 (session `dazzling-taussig-f58f4c`): an in-progress ARC-071
substrate change was stashed this way mid-session and recovered from `stash@{0}` only
because the session noticed its own edits had disappeared from `git status`. That entry has
since been popped. The five entries triaged below are the ones that were already sitting
behind it.

**Nothing audits this.** See "Coverage gap" at the end.

---

## Verdicts

| # | Date (local) | Stash SHA | Apparent owning work | Verdict |
|---|---|---|---|---|
| 0 | 2026-07-27 08:21 | `604e24f0c2` | ARC-070 / MECH-321 policy decomposition + ARC-071 depth cap | ALREADY-LANDED (superseded) |
| 1 | 2026-07-27 07:03 | `66f3356e91` | SD-082 rule-readout consumer | **ALREADY-LANDED (proven)** |
| 2 | 2026-07-24 13:46 | `64a31b95be` | SD-070 P0a / substrate-hash under-inclusion fix | **ALREADY-LANDED (proven)** |
| 3 | 2026-07-22 20:53 | `a9e01fd99c` | ARC-071/MECH-323 (810) + SD-078/SD-079 (806/807) + ARC-063 | ALREADY-LANDED (superseded) |
| 4 | 2026-07-20 02:19 | `87404723f6` | z_world encoder-guard fanout + ARC-108/ARC-110 pack_writer migration | ALREADY-LANDED (superseded) |

**No entry is GENUINELY-ORPHANED.** Every one of the five carries work that reached
`origin/main` by another route. Nothing needs restoring, and nothing needs flagging as lost.

The two verdict grades differ only in strength of proof:

- **proven** -- every hunk in the stash reverse-applies cleanly against `origin/main`
  (`git apply --cached -R --check` into a temp index seeded from `origin/main`), i.e. the
  change is textually contained in trunk today.
- **superseded** -- main has moved *past* the stash, so hunks no longer reverse-apply, but
  (a) every symbol and config field defined in the stash exists on `origin/main`, (b) a
  named landing commit implements exactly that work, and (c) where the stash queued an
  experiment, that experiment has since run and has an evidence manifest. The textual
  residual is comment prose, an earlier draft of a file main has since restructured, a
  DB-authoritative queue snapshot, or a regenerable derived artifact.

---

## Method

Three tests, weakest to strongest, run per stash per file:

1. **Blob identity** -- `git rev-parse 'stash@{N}:<path>'` vs `git rev-parse 'origin/main:<path>'`.
2. **Hunk containment** -- `git diff 'stash@{N}^' 'stash@{N}' -- <path> | git apply --cached -R --check -`
   against a temp index (`GIT_INDEX_FILE`) seeded from `origin/main`. A clean reverse-apply
   proves the change is present on trunk.
3. **Symbol containment** -- every `def`/`class` name and every dataclass field defined in
   the stashed file must exist in `origin/main`'s version. Catches the case where main has
   moved textually but is a strict functional superset.

Test 2 is **conservative in one direction only**: a clean reverse-apply is proof of
containment, but a failure is *not* proof of loss -- it fires whenever main's context lines
have moved, which is the normal case for a five-to-eight-day-old stash. That asymmetry is
why test 3 exists, and why the "superseded" grade is not simply "unclear".

---

## Per-entry evidence

### stash@{0} -- 2026-07-27 08:21 -- `604e24f0c2` -- ARC-070 / MECH-321 -- ALREADY-LANDED (superseded)

9 files, +563/-3. `ree_core/policy/policy_decomposition.py` (+167),
`tests/contracts/test_arc070_policy_decomposition.py` (+155), `ree_core/utils/config.py` (+64),
`hippocampal/event_segmenter.py`, `hippocampal/module.py`, `policy/__init__.py`, `agent.py`,
`tests/test_flag_inertness.py`, `CLAUDE.md`.

- Hunk containment: 5/9 files contained; 4 not (context moved).
- Symbol containment: **0 symbols absent from main across all 9 files.** Main is a strict
  superset everywhere (e.g. `policy_decomposition.py` stash 49 symbols / main 51;
  `config.py` stash 1019 fields / main 1031).
- The headline residual, `depth_cap_config_issues()`, **is on main** at
  `ree_core/policy/policy_decomposition.py:295`, in a *more* developed form than the stash's
  -- main's takes an optional third argument and handles `derived_chunk_max_depth` for the
  growable-ceiling case, which the stash's version predates.
- Landing commits: `2771a8e` "MECH-321: warn on an inert or degenerate
  decomposition_depth_cap (spike 5a)", `7c201f7` "ARC-071: chunk DEPTH becomes a growable
  ceiling derived from the deliberation budget (default OFF)", plus `9a6e7f3`, `2422632`.
- Remaining textual delta is comment prose only (7 lines of docstring/error-message wording
  in `policy_decomposition.py`, 1 comment line in `config.py`).
- **Coupled set intact:** implementation (`policy_decomposition.py`) and its pinned contract
  (`test_arc070_policy_decomposition.py`) are *both* symbol-supersets on main and landed
  together. No half-landed pair.

### stash@{1} -- 2026-07-27 07:03 -- `66f3356e91` -- SD-082 -- ALREADY-LANDED (proven)

4 files, +241/-11. `ree_core/pfc/lateral_pfc_analog.py` (+83),
`tests/contracts/test_sd082_rule_readout_consumer.py` (+154), `agent.py`, `utils/config.py`.

- Blob identity: 2/4 byte-identical to main (`lateral_pfc_analog.py`,
  `test_sd082_rule_readout_consumer.py`).
- Hunk containment: **4/4 reverse-apply cleanly.** Every hunk is on trunk.
- Added-line presence: 215/215 added lines present on main (100%).
- Landing commits: `d4f7580` "SD-082: common-mode-invariant trained rule_state->action-bias
  read-out consumer", `5d243ee` "SD-082 AMEND: head-internals instrumentation for the
  still-zero V3-EXQ-822a propagation".
- Coupled set intact: consumer + its contract both byte-identical to main.

### stash@{2} -- 2026-07-24 13:46 -- `64a31b95be` -- SD-070 P0a / substrate-hash -- ALREADY-LANDED (proven)

3 files, +95/-411. `experiments/v3_exq_724_competence_localization_diagnostic.py`,
`experiments/v3_exq_734_env_difficulty_competence_recovery_sweep.py`,
`tests/contracts/test_zworld_p0_adoption_reaches_every_driver.py`.

- Blob identity: **3/3 byte-identical to `origin/main`.** Strongest possible result -- the
  stashed tree for these paths *is* trunk's tree.
- Hunk containment: 3/3 reverse-apply cleanly (redundant, given blob identity).
- Landing commit: `0332c47` "Close substrate-hash under-inclusion: collapse
  `_train_all_on_agent` onto `experiments/_lib/allon_training.py`".
- The large deletion count (-411) is that collapse: code moved out of the two drivers into
  the shared `_lib` module so its bytes fall inside `arm_fingerprint`'s substrate glob.

### stash@{3} -- 2026-07-22 20:53 -- `a9e01fd99c` -- ARC-071/MECH-323 + SD-078/079 + ARC-063 -- ALREADY-LANDED (superseded)

20 files, +2661/-448.

- Hunk containment: 8/20 contained; 12 not.
- Symbol containment: **0 symbols absent from main across every residual file.**
- Per-residual resolution:
  - `.gitignore` -- the stash adds `traces/`; main has the anchored form `/traces/` at
    line 17. Landed, refined.
  - `experiment_queue.json` -- the stash's V3-EXQ-810 entry is absent from main's queue
    **because the experiment ran**: evidence manifest
    `v3_exq_810_arc071_chunk_accumulator_readiness_20260723T222726Z_v3.json` exists. Same
    for 806/807 (manifests dated 2026-07-25). The queue is DB-authoritative under Phase 3,
    so a 2026-07-22 queue snapshot has no standing regardless.
  - `v3_exq_724` / `v3_exq_734` -- the residual lines describe moving `_train_all_on_agent`
    into `experiments/_lib/allon_training.py`. That file **exists on main**, landed as
    `0332c47`. The stash holds an intermediate draft of a refactor whose finished form is
    on trunk.
  - `tests/contracts/test_zworld_p0_adoption_reaches_every_driver.py` -- main's version is
    strictly *later*: it carries a `_train_all_on_agent_source_module()` helper documented
    "As of 2026-07-23", resolving the definition site via `__module__` to stay correct for
    both the collapsed and the vendored shape. The stash is the 2026-07-22 predecessor.
  - `config.py` (3 lines), `test_flag_inertness.py` (2 lines), `CLAUDE.md` -- comment prose.
- Landing commits: `57a2246` "ARC-071 policy_composition_via_repeated_grounding: MECH-323
  formation + MECH-324 maintenance + MECH-322 sleep-replay carve-out, default OFF",
  `0ec3ef6` "SD-078 + SD-079: common-mode-invariant (centered) context keys", `42895f6`,
  `1d04e51` (ARC-063 CRF).
- Coupled sets intact: `e3_selector.py`, `candidate_rule_field.py`, `anchor_set.py`,
  `latent/stack.py` are all byte-identical to main; their contracts
  (`test_mech423_inference_convergence.py`, `test_flag_inertness.py`) are symbol-supersets
  on main.

### stash@{4} -- 2026-07-20 02:19 -- `87404723f6` -- z_world encoder guard + ARC-108/110 -- ALREADY-LANDED (superseded)

23 files, +7559/-3033.

- Hunk containment: 15/23 contained; 8 not.
- Symbol containment: 0 absent, **except** 9 in
  `v3_exq_734_env_difficulty_competence_recovery_sweep.py` -- `_train_all_on_agent` and 8 of
  its locals (`train_env`, `transition_buffer`, `ep_buf`, `outcome_buf`, `action_prev`,
  `z_self_prev`, `pending_capture`, `p1_snap_summaries`). **All nine are present in
  `origin/main:experiments/_lib/allon_training.py`** (9, 3, 3, 3, 14, 4, 4, 5, 5 occurrences
  respectively), and main's x734 re-imports the function at line 224
  (`from experiments._lib.allon_training import _train_all_on_agent, E2_TRAIN_IN_P1`) so
  `x734._train_all_on_agent` still resolves for its 737/742/808/`mech457_fanout` callers.
  They relocated; they were not lost.
- Per-residual resolution:
  - `experiments/_lib/zworld_encoder_guard.py` -- on main with 21/21 symbols and three
    *later* refining commits: `9f72532` "lift untrained-z_world-encoder detection into _lib",
    `f2e8e2f` "fan out untrained-encoder detection into 728/734/737/742 (detection only)",
    `7c07485` "document which manifest key each policy uses".
  - `v3_exq_728` / `734` / `737` / `742` -- all four use the guard heavily on main
    (22 / 36 / 7 / 18 references). The residual lines are guard docstring/comment wording.
  - `experiment_queue.json` -- 2026-07-20 snapshot; entries have since run. DB-authoritative.
  - `.ua/knowledge-graph.json`, `.ua/meta.json` -- **regenerable derived artifacts** from the
    `/understand` plugin, not source. The stash holds a 2026-07-19T01:29:32Z / 478-file
    analysis; main holds a 2026-07-20T01:30:55Z / 140-file one. These genuinely diverge
    (different scope), but the loss is zero: rerun `/understand ree-v3/`. This is the only
    real content difference anywhere in the five entries, and it is not work.

---

## Actions taken

**All five dropped. The ree-v3 stash list is now EMPTY.** Every one was archive-tagged first
(see below), so no content was destroyed.

Dropped in two passes, deliberately:

1. **First pass -- the two proven contained on `origin/main`:**
   - `66f3356e916c7dee4c60f888a0cdbf1008c06204` -- SD-082, all 4 hunks reverse-apply.
   - `64a31b95be5bbf09f700d9e65ab9a62584c12138` -- SD-070 P0a, all 3 blobs identical.
2. **Second pass -- the three superseded-but-not-byte-proven, on explicit user
   authorisation** ("drop them with archive tag", 2026-07-28):
   - `604e24f0c2c92da8e52cb790c7313cdb30c1986f` (ARC-070/MECH-321, 9 files)
   - `a9e01fd99cf31e10d7b6db998d2a6be7b6aa0e18` (ARC-071/MECH-323 + SD-078/079 + ARC-063, 20 files)
   - `87404723f6dfe86d40a50e6320b039567d2b7dcd` (z_world guard + ARC-108/110, 23 files)

**The two-pass split is the point, not bureaucracy.** Pass 1 was mechanically proven and
needed no permission. Pass 2 rested on a symbol-superset argument plus named landing commits
-- strong, but an *argument*, so it was reported and left for the owner to decide rather than
actioned on a judgement call. Preserve that distinction if this triage is ever repeated.

Nothing was restored. Per CLAUDE.md remedy (b), a judgement-call restore onto a moved trunk
is worse than leaving the entry alone -- and here the judgement call does not even arise,
since main is ahead of all five.

**Every dropped entry was archived as a local tag before being let go**, following the
convention established 2026-07-18 (session `fervent-tereshkova-2f1c69`, WORKSPACE_STATE
2026-07-18T17:39Z) for the 58-stash fleet clear. `ree-v3` now carries six such tags -- the
five below plus `stash-archive/20260714-32c6fd21` from that earlier sweep:

```
stash-archive/20260727-604e24f0  -> 604e24f0c2c92da8e52cb790c7313cdb30c1986f   ( 9 files)
stash-archive/20260727-66f3356e  -> 66f3356e916c7dee4c60f888a0cdbf1008c06204   ( 4 files)
stash-archive/20260724-64a31b95  -> 64a31b95be5bbf09f700d9e65ab9a62584c12138   ( 3 files)
stash-archive/20260722-a9e01fd9  -> a9e01fd99cf31e10d7b6db998d2a6be7b6aa0e18   (20 files)
stash-archive/20260720-87404723  -> 87404723f6dfe86d40a50e6320b039567d2b7dcd   (23 files)
```

File counts were re-verified through the tags *after* the drops (`git stash show --name-only
<tag>`), which is the check that actually proves the content survived the drop rather than
merely that a tag exists.

The tags keep the commits reachable, so the content **cannot be garbage-collected**:
`git stash apply stash-archive/<tag>` or `git show <tag>:<path>` restores it. They are
**LOCAL-ONLY and deliberately never pushed** (verified `git ls-remote --tags origin
'stash-archive/*'` = 0). List with `git tag -l 'stash-archive/*'` -- ree-v3 now has three,
including `stash-archive/20260714-32c6fd21` from the earlier sweep. **Do not bulk-delete
these tags**; deleting them is the one action that would actually destroy the content.

A plain `git stash drop` leaves the commit reachable only until `git gc` prunes it, so the
raw SHAs recorded in the verdict table above are a weaker handle than the tags. Tag first,
then drop.

---

## Coverage gap (reported, not built)

`ree-v3` substrate paths have **no** claim-aware autostash protection, and there is **no**
audit that surfaces a growing stash list to a session.

1. **The claim-aware skip is `REE_assembly`-only.**
   `runner_remote_control._active_claim_on_evidence_dir(ree_assembly_path)` (ree-v3
   `runner_remote_control.py:264`) takes a `REE_assembly` path and matches active
   `TASK_CLAIMS.json` claims against `evidence/` and `docs/claims/` prefixes. Its three call
   sites (`runner_remote_control.py:746,837`, `experiment_runner.py:1373`) all guard
   `REE_assembly` pushes. Nothing equivalent guards the **ree-v3** pull at
   `experiment_runner.py:971/1017/1037`, which is the one that produced all five entries
   here. This matches the CLAUDE.md High-Contention Files section, which documents the
   hazard for `REE_assembly/evidence/**` and `docs/claims/` and is silent on ree-v3
   substrate.

2. **The existing stash warning is the wrong shape for this failure.**
   `experiment_runner._warn_on_stash_bloat()` (line 557) exists, but:
   - it fires at `threshold=20`, and this incident sat at **5**;
   - it prints to the *runner's* stdout on a machine running experiments -- a Claude session
     editing the shared Mac checkout never sees it;
   - its docstring frames the signal as a "scarred-timeline indicator that no longer matters
     operationally" (the cloud-3 191-entry case), i.e. as **hygiene**. The dangerous case is
     the opposite: *one* entry holding a session's live work. A threshold tuned for 191 is
     structurally incapable of catching 1.

Two candidate fixes, both `complicated (buildable)` -- neither built here, and the second is
the one that actually addresses the confirmed failure:

- **(a) Extend the claim-aware skip to ree-v3.** Generalise `_active_claim_on_evidence_dir`
  to take a repo + prefix set, and gate the ree-v3 pull on an active claim covering
  `ree_core/`, `experiments/`, or `tests/`. Prevents the stash from being taken at all --
  but only for sessions that opened a claim naming those paths, which substrate sessions do
  not reliably do today.
- **(b) A session-facing stash audit in `scripts/`.** `grep -rl "stash list" scripts/`
  returns nothing today. A check reporting **any non-empty** ree-v3 stash list -- not a
  bloat threshold -- surfaced at session start (alongside the `TASK_CLAIMS`/`pending_review`
  checks) or in the `/session-land` pre-close sweep would have caught all five of these
  within a day instead of eight. Cheap, and it covers sessions with no claim, which (a)
  cannot.

Recommend (b) first: it is strictly detection, has no interaction with the runner's git
path, and the confirmed failure mode is *silence*, not the stash itself.
