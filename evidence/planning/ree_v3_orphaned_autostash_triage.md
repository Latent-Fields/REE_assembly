# ree-v3 orphaned `autostash` stash triage

**Repo:** `/Users/dgolden/REE_Working/ree-v3` (rounds 1-2). **Round 3 is a different repo on
a different box** -- `~/REE_Working/REE_assembly` on `ree-cloud-3` -- and a different stash
label (`runner-prepull-untracked`, not `autostash`). It is recorded here because the defect,
the method and the archive-tag doctrine are identical; read the round-3 heading for what
does *not* carry over.

**Entries triaged:** 7, across **three rounds**:

| Round | When | Session | Trunk at triage time | Entries |
|---|---|---|---|---|
| 1 | 2026-07-28T05:21Z | `dazzling-solomon-8a0090` | `origin/main` = `04435e0` (`docs: nightly /update-docs 2026-07-28`) | 5 |
| 2 | 2026-07-29T17:13Z | `cranky-blackburn-d11b32` | `origin/main` = `42ab95f` (`SD-083: offline policy-consolidation window`) | 1 |
| 3 | 2026-09-03T05:20Z | `cool-sutherland-9d984d` | `REE_assembly origin/master` = `e892538458` | 1 |

**The stash list was cleared to empty at the end of round 1 and was non-empty again the next
day** -- which is the honest summary of what this defect does. Round 2 exists because the
same runner autostash path produced a fresh entry on 2026-07-29, and because round 1's
three-test method turned out to have a blind spot that would have mis-graded it (see
**Method**, test 4).

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
| 5 | 2026-07-29 17:13 | `936a598dff` | SD-054 `--strict` backlog clear (2 drivers) + INFRA-830-A `criteria_key_correspondence` lint | **INTENTIONALLY-DEAD (proven)** |

**No entry is GENUINELY-ORPHANED.** Every one of the six carries work that reached
`origin/main` by another route, or was deliberately rejected there. Nothing needs restoring,
and nothing needs flagging as lost.

The three verdict grades differ in strength of proof and in *what* they prove:

- **proven** -- every hunk in the stash reverse-applies cleanly against `origin/main`
  (`git apply --cached -R --check` into a temp index seeded from `origin/main`), i.e. the
  change is textually contained in trunk today.
- **superseded** -- main has moved *past* the stash, so hunks no longer reverse-apply, but
  (a) every symbol and config field defined in the stash exists on `origin/main`, (b) a
  named landing commit implements exactly that work, and (c) where the stash queued an
  experiment, that experiment has since run and has an evidence manifest. The textual
  residual is comment prose, an earlier draft of a file main has since restructured, a
  DB-authoritative queue snapshot, or a regenerable derived artifact.
- **intentionally-dead** -- the content is **not** on the tip and never will be, because it
  landed in an *ancestral* commit that was subsequently **reverted on the record**. Proof is
  line-exact containment in that ancestor (test 4), plus the revert commit's own stated
  reasoning. This grade says something the other two do not: the work was not merely
  overtaken, it was **evaluated and rejected**, so restoring it would re-land something trunk
  deliberately removed.

---

## Method

Four tests, weakest to strongest, run per stash per file. Tests 1-3 compare against the
**tip**; test 4 is what you run when all three of them fail:

1. **Blob identity** -- `git rev-parse 'stash@{N}:<path>'` vs `git rev-parse 'origin/main:<path>'`.
2. **Hunk containment** -- `git diff 'stash@{N}^' 'stash@{N}' -- <path> | git apply --cached -R --check -`
   against a temp index (`GIT_INDEX_FILE`) seeded from `origin/main`. A clean reverse-apply
   proves the change is present on trunk.
3. **Symbol containment** -- every `def`/`class` name and every dataclass field defined in
   the stashed file must exist in `origin/main`'s version. Catches the case where main has
   moved textually but is a strict functional superset.
4. **Ancestor containment** -- for every line the stash's *own* diff adds
   (`git diff 'stash@{N}^' 'stash@{N}' -- <path>`, **not** the blob-vs-tip delta -- see
   trap 2 below), is that line present verbatim in some commit **reachable from
   `origin/main`**? Run this when tests 1-3 have all failed, *before* concluding the entry
   is orphaned.

Test 2 is **conservative in one direction only**: a clean reverse-apply is proof of
containment, but a failure is *not* proof of loss -- it fires whenever main's context lines
have moved, which is the normal case for a five-to-eight-day-old stash. That asymmetry is
why test 3 exists, and why the "superseded" grade is not simply "unclear".

### Why test 4 exists (added round 2, 2026-07-29)

**Tests 1-3 all evaluate against the tip, so all three fail on content that landed and was
then reverted -- and that failure reads exactly like "genuinely orphaned".** It is the
opposite: reverted content is the *most* firmly disposed-of content there is, because
someone looked at it on trunk and took it back out. A triage that stops after test 3 will
recover and re-land work that trunk deliberately rejected, which is worse than doing nothing.

Confirmed on entry 5 below: `validate_experiments.py` failed blob identity (`fbd40181a4` vs
tip `d8a711b5d1`), and its 98 added lines are **98/98 present verbatim** in `7b27b1a`, a
permanent ancestor of `origin/main`, which `eeb1eda` reverted four minutes after it landed.

**How to run it.** The stash's own commit timestamp is the strong locator -- an autostash is
taken from a working tree mid-edit, so the commit that finished that work is usually within
minutes of it, not days:

```bash
cd /Users/dgolden/REE_Working/ree-v3
git log -1 --format=%ci 'stash@{N}'                       # when the tree was parked
git log --oneline --since=<that time -1h> -- <path>       # candidate finishing commits
git diff 'stash@{N}^' 'stash@{N}' -- <path>               # what the SESSION added -- NOT blob-vs-tip (trap 2 below)
# then, per candidate: are ALL those added lines in it?
cand=$(mktemp); git cat-file blob "$(git rev-parse '<candidate>:<path>')" > "$cand"   # not `git show` (trap 1 below)
git diff 'stash@{N}^' 'stash@{N}' -- <path> | grep '^+[^+]' | \
  while IFS= read -r l; do grep -qxF -- "${l#+}" "$cand" || echo "ABSENT: ${l#+}"; done
```

Zero `ABSENT` lines is the proof. Then confirm the candidate is genuinely reachable --
`git merge-base --is-ancestor <candidate> origin/main` -- since a commit that only ever
existed on a dropped branch is not a safe home for the content.

**`stash@{N}` may be substituted with a `stash-archive/*` tag throughout**, which is how this
recipe was verified after entry 5 had already been dropped (`ABSENT count: 0`, candidate
reachable). That matters: once an entry is dropped, the tag is the only handle, so a triage
method that only worked on live stash refs could never be re-checked. Prefer the tag even
while the entry is live -- it is a fixed reference, whereas `stash@{0}` moves under you every
time the runner ticks.

**Two things to check before grading INTENTIONALLY-DEAD, both of which entry 5 exhibited:**

- **Read the revert's commit message and cite it.** A revert is evidence of a decision, and
  the decision's *reasoning* is what distinguishes "rejected" from "backed out to unblock a
  release and will return". Only the former is safe to drop.
- **Check the direction of containment.** The stash may be a strict *subset* of the ancestor
  (an earlier draft) rather than equal to it. That strengthens the verdict -- there is
  nothing in the stash the ancestor lacks -- but it also means the stash blob may be
  **internally broken** and must never be applied. Compare both ways:
  `git diff <ancestor>:<path> 'stash@{N}:<path>'`, and read the added-line count as well as
  the removed one.

### Two mechanical traps the recipe above used to walk straight into (added 2026-08-18)

Both were surfaced grading umbrella stash `93c953009a`, and **both produce a false
GENUINELY-ORPHANED verdict** -- that is, both push the triager toward *restoring* content that
is already on trunk. Worked example with the full measured numbers:
`evidence/planning/umbrella_stash_triage_20260812_93c95300.md`. (That entry was hand-taken
rather than an `autostash`; the traps are properties of the stash object and of the diff being
asked for, so they apply to either.)

**Trap 1 -- a stash is a MERGE COMMIT, so `git show <stash>` hands you the commit, not the
blob.** `git stash push -u` writes an *octopus* merge -- three parents: HEAD, the index commit,
the untracked commit (the 2026-08-18 entry's were `0f76618e`, `ebcf374f`, `8ac1bd87`). Every
pathspec form -- `git show <stash>`, `git show <stash> -- <path>`, `git show <stash> <path>` --
prints the commit header plus a combined `diff --cc` and **exits 0**, so a redirect captures
commit text and every downstream line count, containment check and diff is silently wrong.
Measured: **1088 "lines" captured for a 3407-line file**. The `-- <path>` does not narrow the
output to the file; it only filters which paths the combined diff covers.

Use the two-step form, which cannot resolve to anything but a blob:

```bash
git cat-file blob "$(git rev-parse 'stash@{N}:<path>')" > /tmp/stash_blob
```

Reproduced 2026-08-18 on git 2.34.1 against a synthetic `git stash push -u`: the pathspec forms
return the commit (3414 lines for a 3400-line file), `rev-parse` + `cat-file blob` returns 3400.
On that version the *colon* form `git show 'stash@{N}:<path>'` does resolve correctly, whereas
the 2026-08-18 triage recorded the colon form as failing -- so do not assume either is safe on
your git. `rev-parse` + `cat-file blob` is unambiguous on both.

Same family, also measured that day: `git diff '<rev>:<path>' '<stash-sha>'` -- a blob spec on
one side and a bare commit on the other -- is a **usage error, exit 129**, not a diff. Both
sides need the `:<path>`.

**Trap 2 -- test 4 is applied to the session's OWN added lines, never to the blob-vs-tip
delta.** Test 4 asks "for every line the stash *adds*, is it on trunk?". Computing that set as
`git diff 'origin/main:<path>' 'stash@{N}:<path>'` answers a different question once trunk has
moved: the stash blob is an *older base* plus a small edit, so the diff is dominated by trunk's
own evolution, and pre-existing code that trunk has since restructured is reported as
"added by the stash" (and trunk's new code as "deleted by it"). Measured on
`scripts/igw_routine_tick.py` in the 2026-08-18 entry: blob-vs-tip reported **82 insertions /
794 deletions**, with **54 of the 82 added lines absent from `origin/master`** -- which reads as
major loss and is entirely an artifact of trunk growing 3360 -> 4119 lines in the six days since
the stash was taken. The stash's own diff, `git diff 'stash@{N}^' 'stash@{N}' -- <path>`, yields
the 58 lines the session actually wrote, of which **0 were absent**: fully contained. `<stash>^`
is the first parent, i.e. the commit the working tree was parked on top of.

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

### stash@{0} (round 2) -- 2026-07-29 17:13 -- `936a598dff` -- SD-054 backlog + INFRA-830-A lint -- INTENTIONALLY-DEAD (proven)

3 files, +414/-4. Found by `audit_stashes.py` -- i.e. by the round-1 "coverage gap" fix
below, working as intended, on its first live catch of a new entry.

- **Blob identity: 2/3 byte-identical to `origin/main`.**
  `experiments/v3_exq_603e_q045_mech313_mech260_scaffolded_sd054.py` (`0e2ba9ac88`) and
  `experiments/v3_exq_622_goal_stream_staged_sd054.py` (`58c1fb38b5`) both landed as
  `55a8fc2742` ("SD-054 drivers: clear the pre-existing `--strict` validator backlog").
- **`validate_experiments.py` DIFFERS**: stash `fbd40181a4`, tip `d8a711b5d1`. Tests 1-3 all
  fail on it. This is the file that motivated test 4.
- **Ancestor containment: 98/98 added lines present verbatim in `7b27b1a`**
  ("validate_experiments: `criteria_key_correspondence` lint"), which
  `git merge-base --is-ancestor 7b27b1a origin/main` confirms is reachable.
- **Reverted on the record by `eeb1eda`**, four minutes after `7b27b1a` landed: *"it encodes
  a convention that does not exist"*. Its measurements: **101** of ~1100 experiment scripts
  fire as specified, **23** under the narrowest useful variant, **8** requiring apparent 1:1
  intent -- **zero true positives in every variant**, and no variant would have caught
  V3-EXQ-830 itself once the indexer-side prefix-tolerant join landed (REE_assembly
  `30b997a313` + follow-up). `criteria_non_degenerate` keys legitimately name non-criteria
  (`preconditions_met`, `enough_divergent_seeds`, `gate_a_occupancy`), which is what that
  block *is*. So this is a rejection on evidence, not a temporary backout.
- **The stash is a strict SUBSET of `7b27b1a`, and is broken.** Against the ancestor it adds
  2 lines (both re-flows of pre-lint lines) and removes 18: the `CHECK_NAMES` registration,
  the `criteria_key_warnings` declaration, and the report block. It therefore *uses*
  `criteria_key_warnings` at its line 4940 while never declaring it, and omits
  `criteria_key_correspondence` from `CHECK_NAMES`. **Never apply this blob.**
- **Timing settles it.** The autostash was taken at `17:13:27 +0100`; `7b27b1a` was committed
  **17 seconds later** at `17:13:44 +0100`. The runner caught a mid-edit snapshot of work its
  author finished and committed immediately afterwards -- the clearest possible illustration
  of why the stash timestamp is the right locator for test 4.
- **Circumstance worth recording:** this entry was produced during the 2026-07-29 ree-v3
  rebase-abort loop (WORKSPACE_STATE 2026-07-29T16:45Z), which had already escalated to a
  detached HEAD. `mech-244-experiment-84dce1` archive-tagged it **before** its ref surgery
  and deliberately left it in place rather than drop it mid-repair -- the right call, and the
  reason it was still available to grade properly the next hour.
- **Correction to that session's containment note:** it recorded `validate_experiments.py` as
  matching `origin/main`. It does not (blobs above). Its *conclusion* -- safe to let go --
  was right; its stated *reason* was not, and the distinction is exactly what test 4 is for.
- The session that authored the lint (`cranky-blackburn-d11b32`, WORKSPACE_STATE
  2026-07-29T17:22Z) had reported these edits as swept and **"unrecoverable"** because the
  stash list read empty at the time. They were recoverable throughout; the loss report was
  wrong, harmlessly, since `7b27b1a` already carried a superset.

### Round 3 -- 2026-09-02 17:50 -- `b6c09a3fc0` -- V3-EXQ-571c manifest (REE_assembly on ree-cloud-3) -- ALREADY-LANDED (proven)

**Not a `ree-v3` entry and not an `autostash` entry.** One `runner-prepull-untracked` stash
in `~/REE_Working/REE_assembly` on `ree-cloud-3`, holding exactly **one untracked file**:
`evidence/experiments/v3_exq_571c_e3_variance_monopoly_presence_936_regime_20260902T152856Z_v3.json`
(397,083 bytes, valid JSON, `outcome: FAIL` -- complete, not a partial write).

Surfaced by the 2026-09-03 morning digest via `runner_git_health.py`, graded **AT_RISK**
("hold content proven nowhere else -- DO NOT drop"). That grade was a **false positive**; see
the defect note at the end of this entry.

- **The file is in the third parent, not the stash commit.** `git rev-parse 'stash@{0}:<path>'`
  fails with *"exists on disk, but not in `stash@{0}`"*, which reads like the content is
  missing. It is not: a `runner-prepull-untracked` entry parks **untracked** files, so they
  live in `stash@{0}^3`. Parents were `baf49416` / `dcbd7613` / `01735142` -- trap 1 above, in
  its untracked-file form. Use `<ref>^3:<path>`.
- **Containment chain, proven key-by-key** (blob shas, all on `ree-cloud-3`):

  | Version | Blob | Delta from the stash copy |
  |---|---|---|
  | stash (`^3`) | `df903679` | -- the runner's raw local write |
  | `ee59667eeb` *phase3 writer* | `47584359` | **+`queue_id` only. Zero stash-only keys, zero differing shared values.** |
  | `0ade914d46` *governance* | `cb87ba1a` (= `origin/master`) | +`evidence_direction_note`; `evidence_direction` `diagnostic` -> `non_contributory` |

  So every key **and value** of the stash blob is present verbatim on `origin/master` except
  the one field governance deliberately rewrote. This is whole-value containment of every
  key, which is *stronger* than test 4's line-level check.
- **The content never needed rescuing, because it never travelled by git in the first place.**
  Under Phase 3 a result manifest reaches origin through the coordinator spool
  (`POST /result` -> `phase3_git_writer`), which is what `ee59667eeb` is. The stashed file was
  only ever the runner's **local artifact** of that same write. Worth stating plainly: on a
  Phase-3 worker, a stashed evidence manifest is a *copy*, not a *strand*, unless the spool
  route can be shown to have failed.
- **Restoring it would have been actively harmful.** The single differing field is a
  governance ratification landed 2026-09-02 from confirmed
  `failure_autopsy_V3-EXQ-571c_2026-09-02.json` (`b98e2ccd45`, verified reachable from
  `origin/master`). Applying the stash would revert `non_contributory` back to `diagnostic`.
  This is the round-2 INTENTIONALLY-DEAD hazard in a new dress: the delta is not staleness,
  it is a decision.
- Worktree state was clean for that path throughout -- the on-disk file hashed to `cb87ba1a`,
  identical to `origin/master`. Nothing on the box was at risk.
- **Archive tag:** `stash-archive/20260902-b6c09a3f` -> `b6c09a3fc0920216e751bc4c41cd3883bc31b5dd`,
  local-only on `ree-cloud-3`, 8-char form per the convention below. Verified to resolve
  *before* the drop and re-verified *after* it (`df903679`, md5 `2676692d...`, 397,083 bytes,
  still parsing as JSON) -- the post-drop check is the one that proves survival.
- **Dropped on explicit user authorisation** (2026-09-03, "Drop it"), consistent with the
  two-pass split above: mechanically proven, but the drop happens on a *shared box a session
  does not own*, so it was put to the owner rather than actioned unilaterally.

**Defect found in the grader itself, and it is the reusable finding here.**
`_path_contained` in `runner_git_health.py` (inside the `UNTRACKED_PY` string constant, so
its functions are **not** module attributes -- `import runner_git_health; h.is_superset`
raises `AttributeError`) documents that it tolerates "a reviewer note / changed
`evidence_direction`". Its predicate does not:

```python
def is_superset(origin, local):
    for k, v in local.items():
        if k not in origin or origin[k] != v:
            return False
    return True
```

An **added** key passes; a **changed** shared key fails. Governance rewrites
`evidence_direction` in place, so the docstring's own stated case is the case the code fails
-- confirmed empirically on this pair (`is_superset(origin, stash) -> False`, sole breaking
key `evidence_direction`). Every governance-ratified run whose direction was *changed* rather
than merely annotated therefore grades AT_RISK indefinitely, which is the dangerous direction
for a false positive: it tells the reader not to drop, on every digest, until a real AT_RISK
entry reads as more noise. Routed as `chip-20260903-prepull-grader-changed-field`, which also
asks whether the sibling `_json_content_contained`
(`ree-v3/experiment_runner.py:880`, used by the runner's own pop-time reaper) shares it --
that one *acts* rather than reports, so its error direction must be checked before touching it.

---

---

## Actions taken

**All six dropped. The ree-v3 stash list is EMPTY as of 2026-07-29T17:13Z** (re-verified:
`git stash list` returns 0 entries). Every one was archive-tagged first (see below), so no
content was destroyed. Round 3 (2026-09-03) adds a seventh entry in a *different repo on a
different box*; it did not change ree-v3's state.

### Round 1 (2026-07-28) -- five entries

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

### Round 2 (2026-07-29) -- one entry

`936a598dff4775d1ca2342caf11541b4f2216ef8` dropped as **pass 1** -- mechanically proven, so
no permission was sought, consistent with the split above. The proof is line-exact
containment in an ancestor (test 4) rather than identity with the tip, which is a *stronger*
result than round 1's pass-1 grade, not a weaker one: 2 of 3 blobs were byte-identical to
`origin/main` and the third was 98/98 contained in `7b27b1a`.

Sequence, in the order it must be done:

1. `mech-244-experiment-84dce1` had already tagged it `stash-archive/20260729-936a598` during
   the rebase-loop repair and left it in place. **Re-verified the tag resolved** before doing
   anything else -- an inherited tag is not evidence until you check it.
2. **Re-checked `stash@{0}` was still `936a598dff` at drop time.** Non-negotiable here: the
   runner autostashes every tick, so `stash@{0}` is a *moving* reference. Drop by verified
   sha, never by position taken on trust from an earlier reading.
3. Dropped, then **re-verified after the drop** that all three files and the `fbd40181a4`
   blob still resolve through the tag.

A duplicate 8-character tag created in this round was deleted, leaving one tag per object.
**No edit was made to `validate_experiments.py`** -- `task_claim.py open` returned exit 3 on
it (`keen-elion-70debb` held the earlier claim for unrelated `dead_z_goal_stream` work), and
the verdict required no write to it, so the claim was re-scoped to `ree-v3/.git/refs`.

### Round 3 (2026-09-03) -- one entry, `REE_assembly` on `ree-cloud-3`

`b6c09a3fc0920216e751bc4c41cd3883bc31b5dd` archive-tagged as
`stash-archive/20260902-b6c09a3f` (local-only on that box), then dropped **on explicit user
authorisation**. `git stash list` on `ree-cloud-3`'s `REE_assembly` is empty as of
2026-09-03T05:22Z, and `runner_git_health.py --host ree-cloud-3` no longer reports the entry.

Three things this round adds that rounds 1-2 could not:

1. **The two-pass split needs a third input: whose box is it.** The entry was mechanically
   proven (whole-value containment, stronger than round 2's pass-1 grade), so by the round-1
   rule it was a pass-1 drop needing no permission. It was still put to the owner, because
   the drop mutates a **shared worker** rather than the Mac. Proof strength decides whether a
   drop is *defensible*; ownership of the box decides whether it is *yours to make*.
2. **On a Phase-3 worker, a stashed evidence manifest is a copy, not a strand.** Manifests
   travel by the coordinator spool, so the git-side file is a local artifact of a write that
   already reached origin by another route. Check the spool route *before* treating such an
   entry as a rescue.
3. **The grader can be wrong in the DO-NOT-DROP direction**, and that is the direction that
   rots quietly -- it never loses data, it just trains the reader to skim past AT_RISK. See
   the `is_superset` defect at the end of the round-3 entry above.

### Archive tags

**Every dropped entry was archived as a local tag before being let go**, following the
convention established 2026-07-18 (session `fervent-tereshkova-2f1c69`, WORKSPACE_STATE
2026-07-18T17:39Z) for the 58-stash fleet clear. `ree-v3` now carries **eight** such tags
(verified `git tag -l 'stash-archive/*'`, 2026-07-29T17:13Z):

```
stash-archive/20260729-936a598   -> 936a598dff4775d1ca2342caf11541b4f2216ef8   ( 3 files)
stash-archive/20260729-50c3ea0   -> 50c3ea076042e583a8288a1d3d8652d18a057b43   ( 2 files)
stash-archive/20260727-604e24f0  -> 604e24f0c2c92da8e52cb790c7313cdb30c1986f   ( 9 files)
stash-archive/20260727-66f3356e  -> 66f3356e916c7dee4c60f888a0cdbf1008c06204   ( 4 files)
stash-archive/20260724-64a31b95  -> 64a31b95be5bbf09f700d9e65ab9a62584c12138   ( 3 files)
stash-archive/20260722-a9e01fd9  -> a9e01fd99cf31e10d7b6db998d2a6be7b6aa0e18   (20 files)
stash-archive/20260720-87404723  -> 87404723f6dfe86d40a50e6320b039567d2b7dcd   (23 files)
stash-archive/20260714-32c6fd21  -> 32c6fd21b6c3f87d5a51606f911331a0576dd17a   ( 1 file )
```

**Count update 2026-08-19: `ree-v3` now carries nine and the umbrella `REE_Working` two,
eleven in total; the block above remains the 2026-07-29 snapshot, not a current list.**

`20260714-32c6fd21` predates this document (the earlier fleet sweep). `20260729-50c3ea0` was
tagged by `gracious-snyder-aa4b35` on 2026-07-29 for the SD-054 driver work it recovered and
re-applied as a patch (`55a8fc2742`); it is **not** an entry triaged here, and it holds the
same two driver files as entry 5's contained pair.

**The short-sha component is 8 characters by convention** -- `20260729-50c3ea0` and
`20260729-936a598` are 7 and are the drift, not the pattern. Match the 8-char form for new
tags; do not rename the existing ones.

File counts were re-verified through the tags *after* the drops (`git stash show --name-only
<tag>`), which is the check that actually proves the content survived the drop rather than
merely that a tag exists.

The tags keep the commits reachable, so the content **cannot be garbage-collected**:
`git stash apply stash-archive/<tag>` or `git show <tag>:<path>` restores it. They are
**LOCAL-ONLY and deliberately never pushed** -- see **Why LOCAL-ONLY** below for the
reasoning, decided 2026-08-19 (re-verified 0 on both origins 2026-07-29 and 2026-08-19:
`git ls-remote --tags origin 'refs/tags/stash-archive/*'`). List with `git tag -l 'stash-archive/*'`. **Do not
bulk-delete these tags**; deleting them is the one action that would actually destroy the
content.

A plain `git stash drop` leaves the commit reachable only until `git gc` prunes it, so the
raw SHAs recorded in the verdict table above are a weaker handle than the tags. Tag first,
then drop.

#### Why LOCAL-ONLY -- the decision and its reasoning (2026-08-19)

The convention above stated "local-only" but never justified it, so it kept being re-raised.
Decided 2026-08-19 (`chip-20260818-stash-archive-tags-local-only`): **local-only is correct;
the tags are NOT pushed.** Recorded here so the next triager does not re-open it.

State at decision time: **11 tags, 0 on any origin** -- 2 in the umbrella `REE_Working`
(private) and 9 in `ree-v3` (**public**). Ten of the 11 are reachable from no branch at all,
so the Mac's local `.git` is their sole copy. The one exception is instructive, and is
reason 2 below.

**1. The content is never what is at risk -- the drop gate is the proof of that.** An entry
is dropped only once its added lines are proven line-exact contained in a commit reachable
from `origin/main` (test 4 above), so for every dropped entry the content is *already on
origin* by construction. An INTENTIONALLY-DEAD entry is the same story one commit further
back: the revert is on origin, so its pre-revert parent holds the content. Losing a tag
therefore loses a redundant packaging of content origin already carries -- never the only
copy of any work. What a tag uniquely holds is the stash *commit object*, i.e. the handle for
re-deriving "what this session had added" via `git diff <tag>^ <tag>`.

**2. The fleet already has the right mechanism for content that must survive, and it is not
an archive tag.** `stash-archive/20260819-dd4b0a4` -- the single tag of the 11 that IS
reachable from origin -- got there because a session put its content on a branch,
`origin/integration/contextmemory-write-selection-436f-salvage`. That is the correct move for
a stash whose content is *wanted*. Archive tags are for residue proven redundant; a salvage
branch is for work that must live. Two jobs, two mechanisms. Pushing archive tags would blur
them, and "is it on origin?" would stop meaning "was it kept?".

**3. Origin's ref namespace is shared operational surface, and `ree-v3` is public.** Pushed
tags land in the public Tags UI, are fetched in full by every fresh `git clone` (how a new
cloud worker is provisioned), and the convention above **forbids bulk-deleting them** -- so
there is no reaping path and the set only grows. Measured 2026-08-19: pushing the unreachable
tags would add **175 objects / ~3.9 MB to public `ree-v3`** and 26 objects / ~6.7 KB to the
private umbrella, at an observed accrual of ~5 tags/month over 2026-07-14 -> 2026-08-19. That
is a permanent, one-way, growing cost on a shared production repo, bought for a per-machine
forensic convenience.

**4. The residual durability gap is a laptop-BACKUP problem, not a git-remote problem.** The
exposure is real and is accepted, not denied: if the Mac's disk is lost, those ten drop
verdicts stop being independently re-runnable and become assertions backed by the written
record in this document. The matched fix is not publication but
`git bundle create <backup-path>/stash-archive-<repo>-<date>.bundle --tags 'stash-archive/*'`
into whatever already covers the laptop -- durability with no shared-namespace cost and no
publication. **Not built here** (this chip was a decision, not a build); named so the option
is on the record if the exposure is ever judged unacceptable.

**Explicitly NOT a reason -- checked, void, do not re-invent it.** The tempting objection is
clinical-hours provenance: all 11 stash commits are personal-identity
(`nooarche <daniel.delaharpe.golden@gmail.com>`), so a raw
`git push origin 'refs/tags/stash-archive/*'` IS held in-window by
`scripts/git-hooks/pre-push`. But the author dates are clean. Every one is outside the Dublin
clinical window, and the single apparent exception -- `20260724-64a31b95`, Fri 2026-07-24
13:46 IST, nominally inside Fri 09:00-14:00 -- falls within the declared annual-leave range
2026-07-18 -> 2026-07-26 in `scripts/clinical_leave.json`, so it is not clinical time at all.
Publication would therefore not have misrepresented clinical hours; the guard's hold is a
scheduling inconvenience, not a provenance argument. The decision rests on 1-4, not on this.

**What this does not license.** Do not delete any `stash-archive/*` tag (unchanged from
above), and do not read "local-only" as "expendable" -- point 4 is an accepted exposure, not
a claim that the tags do not matter. If a specific entry's content is ever judged to need
durability, apply reason 2: put that content on a branch and push the branch.

---

## Coverage gap (round 1: reported, not built -- BOTH SINCE BUILT, see the round-2 status below)

> **Status as of 2026-07-29 (round 2).** Both candidate fixes named at the end of this
> section were built within a day of round 1, and the gap described below is **closed in
> code**. The text is kept because it is the diagnosis the fixes were built against.
>
> - **(b) built first, as recommended** -- `scripts/audit_stashes.py`
>   (`REE_Working 4cc9cb9c35`, "report ANY non-empty stash list, not a bloat threshold"),
>   wired into the Session Startup Protocol step 7 and `/session-land` Phase 2d. Extended
>   2026-07-29 (`0396f02514`) to also catch a repeating rebase-abort loop, the hidden
>   `<git-dir>/rebase-merge/autostash` an in-flight rebase parks outside `git stash list`,
>   and a stuck detached HEAD. **It found entry 5** -- the first live catch of a new entry,
>   within an hour rather than the eight days that motivated it.
> - **(a) built too** -- ree-v3 `4a22888` (2026-07-28T22:10), "extend the claim-aware
>   autostash skip to the ree-v3 pull": `_active_claim_on_ree_v3_code` now gates the pull at
>   `experiment_runner.py:1126` and logs `git pull ree-v3: SKIPPED`, with contracts in
>   `tests/contracts/test_ree_v3_pull_claim_guard.py`.
>
> **One caveat, and it is why entry 5 still happened.** A long-lived runner process predates
> the guard and does not have it: the Mac runner at the time of entry 5 was `r4377 87c3328
> 2026-07-27`, started before `4a22888` landed, with **zero** `SKIPPED` lines in its entire
> log (WORKSPACE_STATE 2026-07-29T17:03Z). **Restarting the runner is what activates (a)**,
> and per CLAUDE.md that is the user's call. Until then (b) is the only live protection --
> which is a good argument for having built the detector first.

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

Two candidate fixes, both `complicated (buildable)` -- **neither built in round 1; both built
by 2026-07-29, see the status box at the top of this section** -- and the second is the one
that actually addresses the confirmed failure:

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

**Round-2 verdict on that recommendation: it held.** (b) shipped first, and it is what caught
entry 5 -- while (a), which shipped a day later, was inert on the live runner because the
process predated it. A detector that works on every session beat a preventer that only works
after a restart. Note the residual asymmetry, though: (b) tells you a stash exists, it does
not tell you it is *yours*. Entry 5's own author had already concluded the work was lost
before the audit surfaced it, so **detection still depends on a session recognising its own
filenames in the report** -- which is exactly what the audit's output text asks the reader to
do, and exactly what did not happen here.
